from django.shortcuts import render, redirect
from dronzaPanel.models import Products, SocialMedia, userBlog, seoTags, MainSlider
from home.models import Place_Order
from cart.cart import Cart
from home.definedEmails import notify_order_confirmation
from dronzaPanel.decorators import custom_login_required


@custom_login_required
def cart_add(request, id):
    cart = Cart(request)

    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("/shop")


@custom_login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.remove(product)
    return redirect('/cart-detail')


@custom_login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect('/cart-detail')


@custom_login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.decrement(product=product)
    return redirect('/cart-detail')


@custom_login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('/cart-detail')


@custom_login_required
def cart_detail(request):
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    SEOTAGS = seoTags.objects.filter(page='cart_detail')
    SLIDER = MainSlider.objects.filter(page='cart_detail_page')

    context = {
        'SMDT': SMDT,
        'RCPST': RCPST,
        'SEOTAGS': SEOTAGS,
        'SLIDER': SLIDER
    }
    return render(request, 'cart_detail.html', context)


@custom_login_required
def checkout(request):
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    SEOTAGS = seoTags.objects.filter(page='checkout_page')
    SLIDER = MainSlider.objects.filter(page='checkout_page')

    context = {
        'SMDT': SMDT,
        'RCPST': RCPST,
        'SEOTAGS': SEOTAGS,
        'SLIDER': SLIDER,
    }

    return render(request, 'checkout.html', context)


@custom_login_required
def place_order(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        status = request.POST.get('status')
        product_ids = request.POST.getlist('product_id')  # Retrieve the list of product IDs
        product_prices = request.POST.getlist('p_price')  # Retrieve the list of product prices
        product_quantities = request.POST.getlist('p_quantity')  # Retrieve the list of product quantities
        product_totals = request.POST.getlist('p_total')  # Retrieve the list of product totals

        product_ids = [int(pid) for pid in product_ids]  # Convert the product IDs to integers
        product_prices = [float(price) for price in product_prices]  # Convert the product prices to floats
        product_quantities = [int(quantity) for quantity in
                              product_quantities]  # Convert the product quantities to integers
        product_totals = [float(total) for total in product_totals]  # Convert the product totals to floats

        product_ids_string = ','.join(
            str(pid) for pid in product_ids)  # Convert the list of product IDs to a comma-separated string
        product_prices_string = ','.join(
            str(price) for price in product_prices)  # Convert the list of product prices to a comma-separated string
        product_quantities_string = ','.join(str(quantity) for quantity in
                                             product_quantities)  # Convert the list of product quantities to a comma-separated string
        product_totals_string = ','.join(
            str(total) for total in product_totals)  # Convert the list of product totals to a comma-separated string

        p_grand_total = request.POST.get('p_grand_total')
        c_name = request.POST.get('c_name')
        c_email = request.POST.get('c_email')
        c_phone = request.POST.get('c_phone')
        c_city = request.POST.get('c_city')
        c_zip = request.POST.get('c_zip')
        c_country = request.POST.get('c_country')
        c_address1 = request.POST.get('c_address1')
        c_address2 = request.POST.get('c_address2')

        reg = Place_Order.objects.create(
            product_id=product_ids_string,
            user_id=user_id,
            status=status,
            p_price=product_prices_string,
            p_quantity=product_quantities_string,
            p_total=product_totals_string,
            p_grand_total=p_grand_total,
            c_name=c_name,
            c_email=c_email,
            c_phone=c_phone,
            c_city=c_city,
            c_zip=c_zip,
            c_country=c_country,
            c_address1=c_address1,
            c_address2=c_address2
        )

        # Sending email to customer
        notify_order_confirmation(c_name, c_email, c_phone, c_city, c_zip, c_country, c_address1, c_address2,
                                  p_grand_total)

        cart = Cart(request)
        cart.clear()

        return redirect('/order-placed')

    return render(request, 'checkout.html')


@custom_login_required
def trackOrder(request):
    user_id = request.user.id
    order_list = Place_Order.objects.filter(user_id=user_id).order_by('-id')[:9]
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    SEOTAGS = seoTags.objects.filter(page='track_order')
    SLIDER = MainSlider.objects.filter(page='track_order_page')
    context = {
        'product_orders': order_list,
        'RCPST': RCPST,
        'SMDT': SMDT,
        'SEOTAGS': SEOTAGS,
        'SLIDER': SLIDER
    }
    return render(request, 'track_order.html', context)
