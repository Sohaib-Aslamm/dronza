from django.shortcuts import render, redirect, HttpResponseRedirect

from dronzaPanel.models import AboutTitlePost, QualityTrust, OurTeam, ServicesTypes, Pricing, Gallery, userBlog, \
    SocialMedia, MainSlider, HomeHIW, HomeHTU, HomeAbout, Products, productImages, HomeSRFP, VideoGallery, \
    WhatPeopleSay, OurPartner, droneParts, dronePartsImages

from home.models import contact_us, productReview, blog_Review, sellYourDrone, sellYourDroneImages, Place_Order

from home.forms import contactForm

from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required

from cart.cart import Cart

from django.contrib.auth.models import User

from home.definedEmails import *
# Create your views here.


def baseTemplate(request):
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    context = {'SMDT': SMDT, 'RCPST': RCPST, }
    return render(request, 'baseHome.html', context)


def index(request):
    MSLDR = MainSlider.objects.all()
    HIWork = HomeHIW.objects.all()
    HTUSE = HomeHTU.objects.all()
    HABT = HomeAbout.objects.all()
    PRDCT = Products.objects.filter(featured='Featured')
    SRFP = HomeSRFP.objects.all()
    HVG = VideoGallery.objects.all()
    OURTM = OurTeam.objects.all()
    WPSDT = WhatPeopleSay.objects.all()
    OPTDT = OurPartner.objects.all()
    UBDT = userBlog.objects.all()[:3]
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    context = {'MSLDR': MSLDR, 'HIWork': HIWork, 'HTUSE': HTUSE, 'HABT': HABT, 'PRDCT': PRDCT, 'SRFP': SRFP, 'HVG': HVG,
               'OURTM': OURTM, 'WPSDT': WPSDT, 'OPTDT': OPTDT, 'UBDT': UBDT, 'RCPST': RCPST, 'SMDT': SMDT}
    return render(request, 'Home.html', context)


def about(request):
    TTDATA = AboutTitlePost.objects.all()
    QTDATA = QualityTrust.objects.all()
    TMDATA = OurTeam.objects.all()
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    context = {'TTDATA': TTDATA, 'QTDATA': QTDATA, 'TMDATA': TMDATA, 'RCPST': RCPST, 'SMDT': SMDT}
    return render(request, 'About.html', context)


def services(request):
    RegularServices = ServicesTypes.objects.filter(type='RegularService')
    MAINSERVICES = ServicesTypes.objects.filter(type='MainService')
    PRCDT = Pricing.objects.all()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    context = {'RegularServices': RegularServices, 'PRCDT': PRCDT, 'RCPST': RCPST, 'SMDT': SMDT,
               'MAINSERVICES': MAINSERVICES}
    return render(request, 'Services.html', context)


def gallery(request):
    GLLRY = Gallery.objects.all()
    GLLRY2 = Gallery.objects.values('category').distinct()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    context = {'GLLRY': GLLRY, 'GLLRY2': GLLRY2, 'RCPST': RCPST, 'SMDT': SMDT}
    return render(request, 'Gallery.html', context)


def shop(request):
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    context = {'RCPST': RCPST, 'SMDT': SMDT}
    return render(request, 'Shop.html', context)


def dronzaShop(request):
    dronzaProducts = Products.objects.all().order_by('-id')
    dronzapaginator = Paginator(dronzaProducts, 50)
    dronzapageNo = request.GET.get('page')
    dronzaProductsFINAL = dronzapaginator.get_page(dronzapageNo)
    dronzatotalPages = dronzaProductsFINAL.paginator.num_pages
    DRONZATGRY = Products.objects.values('category').distinct()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    FEATURED = Products.objects.filter(featured='Featured')

    context = {'dronzaProductsFINAL': dronzaProductsFINAL,
               'dronzalastPage': dronzatotalPages, 'dronzatotalPages': dronzatotalPages,
               'dronzapageList': [n + 1 for n in range(dronzatotalPages)], 'DRONZATGRY': DRONZATGRY,
               'FEATURED': FEATURED, 'RCPST': RCPST, 'SMDT': SMDT}
    return render(request, 'dronzaShop.html', context)


def drone_parts(request):
    PRDCTS = droneParts.objects.all().order_by('-id')
    paginator = Paginator(PRDCTS, 50)
    pageNo = request.GET.get('page')
    PRDCTSFINAL = paginator.get_page(pageNo)
    totalPages = PRDCTSFINAL.paginator.num_pages
    PRDCTGRY = droneParts.objects.values('category').distinct()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    FEATURED = droneParts.objects.filter(featured='Featured')

    context = {'PRDCTS': PRDCTSFINAL, 'lastPage': totalPages, 'pageList': [n + 1 for n in range(totalPages)],
               'PRDCTGRY': PRDCTGRY, 'FEATURED': FEATURED, 'RCPST': RCPST, 'SMDT': SMDT}
    return render(request, 'droneParts.html', context)


def shopDetail(request, id, type):
    if type == 'droneParts':
        shpDetail = droneParts.objects.get(id=id)
        PRDRVW = droneParts.objects.filter(id=id)
        prd_images = dronePartsImages.objects.filter(Product_ID_id=id)
        coments = productReview.objects.filter(product__in=PRDRVW)
        RCPST = userBlog.objects.all().order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()
        return render(request, 'dronepartsDetails.html', {'shpDetail': shpDetail, 'coments': coments,
                                                          'prd_images': prd_images, 'RCPST': RCPST, 'SMDT': SMDT})

    if type == 'dronzaProduct':
        shpDetail = Products.objects.get(id=id)
        prd_images = productImages.objects.filter(Product_ID_id=id)
        RCPST = userBlog.objects.all().order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()

        context = {'shpDetail': shpDetail, 'prd_images': prd_images, 'RCPST': RCPST, 'SMDT': SMDT}
        return render(request, 'dronzashopDetails.html', context)


def customerProduct(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        images = request.FILES.getlist('images')
        name = request.POST.get('name')
        email = request.POST.get('email')
        pPhone = request.POST.get('pPhone')
        sPhone = request.POST.get('sPhone')
        location = request.POST.get('location')
        title = request.POST.get('title')
        price = request.POST.get('price')
        category = request.POST.get('category')
        flight_time = request.POST.get('flight_time')
        camera = request.POST.get('camera')
        color = request.POST.get('color')
        condition = request.POST.get('condition')
        label1 = request.POST.get('label1')
        input1 = request.POST.get('input1')
        label2 = request.POST.get('label2')
        input2 = request.POST.get('input2')
        label3 = request.POST.get('label3')
        input3 = request.POST.get('input3')
        label4 = request.POST.get('label4')
        input4 = request.POST.get('input4')
        description = request.POST.get('description')
        thumbnail = request.FILES['thumbnail']

        sv = sellYourDrone(name=name, email=email, sPhone=sPhone, pPhone=pPhone, location=location, title=title,
                           price=price, category=category, flight_time=flight_time, camera=camera, color=color,
                           condition=condition, label1=label1, input1=input1, label2=label2, input2=input2,
                           label3=label3, input3=input3, label4=label4, input4=input4, description=description,
                           thumbnail=thumbnail, user_id=user_id)
        sv.save()

        latest_id = sellYourDrone.objects.latest('id').id

        for f in images:
            sellerImages = sellYourDroneImages(images=f, Product_ID_id=latest_id)
            sellerImages.save()

    user_id = request.user.id
    SYDProducts = sellYourDrone.objects.filter(user_id=user_id)
    paginator = Paginator(SYDProducts, 8)
    pageNo = request.GET.get('page')
    SYDProductsFINAL = paginator.get_page(pageNo)
    totalPages = SYDProductsFINAL.paginator.num_pages
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()

    context = {'SYDProducts': SYDProductsFINAL, 'lastPage': totalPages, 'pageList': [n + 1 for n in range(totalPages)],
               'RCPST': RCPST, 'SMDT': SMDT}
    return render(request, 'customerProducts.html', context)


def sellDrones(request):
    sellerProducts = sellYourDrone.objects.all()
    paginator = Paginator(sellerProducts, 8)
    pageNo = request.GET.get('page')
    sellerProductsFINAL = paginator.get_page(pageNo)
    totalPages = sellerProductsFINAL.paginator.num_pages
    Product_Category = sellYourDrone.objects.values('category').distinct()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    FEATURED = Products.objects.filter(featured='Featured')
    context = {'sellerProducts': sellerProductsFINAL, 'Product_Category': Product_Category, 'lastPage': totalPages,
               'pageList': [n + 1 for n in range(totalPages)], 'RCPST': RCPST, 'SMDT': SMDT, 'FEATURED': FEATURED}
    return render(request, 'sellDrone.html', context)


def prodReview(request):
    if request.method == 'POST':
        prdSno = request.POST.get('pdsNo')
        author = request.POST.get('author')
        email = request.POST.get('email')
        review = request.POST.get('review')
        prd_id = Products.objects.get(id=prdSno)
        sv = productReview(author=author, email=email, review=review, product=prd_id)
        sv.save()

    return redirect('/shop')


def contactus(request):
    if request.method == 'POST':
        CNTCTFM = contactForm(request.POST, request.FILES)
        if CNTCTFM.is_valid():
            NM = CNTCTFM.cleaned_data['name']
            SBJ = CNTCTFM.cleaned_data['subject']
            EM = CNTCTFM.cleaned_data['email']
            PH = CNTCTFM.cleaned_data['phone']
            MSG = CNTCTFM.cleaned_data['message']
            sv = contact_us(name=NM, subject=SBJ, email=EM, phone=PH, message=MSG)
            sv.save()
            notify_contact_us(NM, EM, MSG)  # send email to customer who contacted by web site
            contactForm()
            return HttpResponseRedirect('/thankyou')
    else:
        CNTCTFM = contactForm()
        SMDT = SocialMedia.objects.all()
        RCPST = userBlog.objects.all().order_by('-sNo')[:2]
        context = {'form': CNTCTFM, 'RCPST': RCPST, 'SMDT': SMDT}
    return render(request, 'contactUs.html', context)


def blog(request):
    BLOGDATA = userBlog.objects.all().order_by('-sNo')
    paginator = Paginator(BLOGDATA, 9)
    pageNo = request.GET.get('page')
    BLOGDATAFINAL = paginator.get_page(pageNo)
    totalPages = BLOGDATAFINAL.paginator.num_pages
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    context = {'BLOGDATA': BLOGDATAFINAL, 'lastPage': totalPages, 'pageList': [n + 1 for n in range(totalPages)],
               'RCPST': RCPST, 'SMDT': SMDT}
    return render(request, 'Blog.html', context)


def postDetail(request, sNo):
    rdPost = userBlog.objects.filter(sNo=sNo)
    coments = blog_Review.objects.filter(post__in=rdPost)
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    context = {'rdPost': rdPost, 'RCPST': RCPST, 'SMDT': SMDT, 'coments': coments}
    return render(request, 'postDetail.html', context)


def blogReview(request):
    if request.method == 'POST':
        postSno = request.POST.get('postSno')
        author = request.POST.get('author')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        post_id = userBlog.objects.get(sNo=postSno)
        sv = blog_Review(author=author, email=email, comment=comment, post=post_id)
        sv.save()
    return redirect('/blog')


def thankyou(request):
    return render(request, 'thanks.html')


def orderDone(request):
    return render(request, 'Order_Done.html')


def error404(request):
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    context = {'RCPST': RCPST, 'SMDT': SMDT}
    return render(request, 'error404.html', context)


def testing(request):
    return render(request, 'testingTemplate.html')


# <------------------------------------------ Cart System ------------------------------------>


@login_required(login_url='/user_login')
def cart_add(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("/dronzaShop")


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

# <------------------------------------------ Detail Of Records ------------------------------------>


def DetailRecord(request, id, type):

    if type == 'User':
        Record = User.objects.get(id=id)
        RCPST = userBlog.objects.all().order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()
        context = {'Record': Record, 'RCPST': RCPST, 'SMDT': SMDT}
        return render(request, 'user_detail.html', context)

    if type == 'MainService':
        Record = ServicesTypes.objects.get(id=id)
        PriceDetail = Pricing.objects.all()
        RCPST = userBlog.objects.all().order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()
        context = {'rec': Record, 'PRCDT': PriceDetail, 'RCPST': RCPST, 'SMDT': SMDT}
        return render(request, 'serviceDetail.html', context)

    if type == 'sellDrone':
        Record = ServicesTypes.objects.get(sNo=id)
        PriceDetail = Pricing.objects.all()
        RCPST = userBlog.objects.all().order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()
        context = {'rec': Record, 'PRCDT': PriceDetail, 'RCPST': RCPST, 'SMDT': SMDT}
        return render(request, 'serviceDetail.html', context)

    if type == 'sellerProduct':
        Record = sellYourDrone.objects.get(id=id)
        product_images = sellYourDroneImages.objects.filter(Product_ID_id=id)
        RCPST = userBlog.objects.all().order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()
        context = {'rec': Record, 'product_images': product_images, 'RCPST': RCPST, 'SMDT': SMDT}
        return render(request, 'sellDrone_Detail.html', context)

    if type == 'teamDetail':
        Record = OurTeam.objects.get(id=id)
        RCPST = userBlog.objects.all().order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()
        context = {'rec': Record, 'RCPST': RCPST, 'SMDT': SMDT}
        return render(request, 'teamDetail.html', context)

    if type == 'order':
        Record = Place_Order.objects.get(id=id)
        p_id = Record.product_id.replace("[", "").replace("]", "").replace("'", "")
        p_id = p_id.split(",")
        product_data = Products.objects.filter(id__in=p_id).values('name', 'image')

        price_total = Record.p_total.replace("[", "").replace("]", "").replace("'", "")
        p_quantity = Record.p_quantity.replace("[", "").replace("]", "").replace("'", "")
        p_price = Record.p_price.replace("[", "").replace("]", "").replace("'", "")

        price_total = price_total.split(",")
        p_quantity = p_quantity.split(",")
        p_price = p_price.split(",")
        RCPST = userBlog.objects.all().order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()
        context = {'Record': Record, 'price_total': price_total, 'p_quantity': p_quantity, 'p_price': p_price,
                   'product_data': product_data, 'RCPST': RCPST, 'SMDT': SMDT}
        if request.method == 'POST':
            Record.status = request.POST.get('status')
            Record.save()
            return redirect('/orders')

        return render(request, 'order_detail.html', context)

    if type == 'track_order':
        Record = Place_Order.objects.get(id=id)
        p_id = Record.product_id.replace("[", "").replace("]", "").replace("'", "")
        p_id = p_id.split(",")
        product_data = Products.objects.filter(id__in=p_id).values('name', 'image')

        price_total = Record.p_total.replace("[", "").replace("]", "").replace("'", "")
        p_quantity = Record.p_quantity.replace("[", "").replace("]", "").replace("'", "")
        p_price = Record.p_price.replace("[", "").replace("]", "").replace("'", "")

        price_total = price_total.split(",")
        p_quantity = p_quantity.split(",")
        p_price = p_price.split(",")
        RCPST = userBlog.objects.all().order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()

        context = {'Record': Record, 'price_total': price_total, 'p_quantity': p_quantity, 'p_price': p_price,
                   'product_data': product_data, 'RCPST': RCPST, 'SMDT': SMDT}
        return render(request, 'track_order_detail.html', context)

# <------------------------------------------ Delete Record -------------------------------------->


def Delete(request, id, type):
    if type == 'sellerProduct':
        DeleteRecord = sellYourDrone.objects.get(id=id)
        DeleteRecord.delete()
        return render(request, 'customerProducts.html')