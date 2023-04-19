from django.shortcuts import render, redirect
from dronzaPanel.models import Products, SocialMedia, userBlog
from home.models import Place_Order
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from home.definedEmails import notify_order_confirmation


@login_required(login_url='/user_login')
def cart_add(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("/shop")


@login_required(login_url='/user_login')
def item_clear(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.remove(product)
    return redirect('/cartDetail')


@login_required(login_url='/user_login')
def item_increment(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect('/cartDetail')


@login_required(login_url='/user_login')
def item_decrement(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.decrement(product=product)
    return redirect('/cartDetail')


@login_required(login_url='/user_login')
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('/cartDetail')


@login_required(login_url='/user_login')
def cart_detail(request):
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    context = {'SMDT': SMDT, 'RCPST': RCPST, }
    return render(request, 'cart_detail.html', context)


@login_required(login_url='/user_login')
def checkout(request):
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    context = {'SMDT': SMDT, 'RCPST': RCPST, }
    return render(request, 'checkout.html', context)


@login_required(login_url='/user_login')
def place_order(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        status = request.POST.get('status')
        product_id = request.POST.getlist('product_id')
        p_price = request.POST.getlist('p_price')
        p_quantity = request.POST.getlist('p_quantity')
        p_total = request.POST.getlist('p_total')
        p_grand_total = request.POST.get('p_grand_total')
        c_name = request.POST.get('c_name')
        c_email = request.POST.get('c_email')
        c_phone = request.POST.get('c_phone')
        c_city = request.POST.get('c_city')
        c_zip = request.POST.get('c_zip')
        c_country = request.POST.get('c_country')
        c_address1 = request.POST.get('c_address1')
        c_address2 = request.POST.get('c_address2')
        reg = Place_Order(product_id=product_id, user_id=user_id, status=status, p_price=p_price, p_quantity=p_quantity,
                          p_total=p_total, p_grand_total=p_grand_total, c_name=c_name, c_email=c_email, c_phone=c_phone,
                          c_city=c_city, c_zip=c_zip, c_country=c_country, c_address1=c_address1, c_address2=c_address2)
        reg.save()

        # sending email to customer
        notify_order_confirmation(c_name, c_email, c_phone, c_city, c_zip, c_country, c_address1, c_address2,
                                  p_grand_total)

        cart = Cart(request)
        cart.clear()
        return redirect('/order_placed')
    return render(request, 'checkout.html')


def trackOrder(request):
    u_id = request.user.id
    product_orders = Place_Order.objects.filter(user_id=u_id).order_by('-id')[:9]
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    context = {'product_orders': product_orders, 'RCPST': RCPST, 'SMDT': SMDT}
    return render(request, 'track_order.html', context)