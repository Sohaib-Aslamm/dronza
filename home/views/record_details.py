from django.shortcuts import render, redirect
from dronzaPanel.models import Products, ServicesTypes, Pricing, OurTeam, SocialMedia, userBlog, productImages
from home.models import Place_Order, sellYourDrone, sellYourDroneImages, productReview
from django.contrib.auth.models import User


def DetailRecord(request, type, slug):
    if type == 'UserList':
        Record = User.objects.get(username=slug)
        context = {'Record': Record}
        return render(request, 'user_detail.html', context)

    if type == 'shop':
        shpDetail = Products.objects.get(slug=slug)
        prd_images = productImages.objects.filter(Product_ID_id=shpDetail.id)
        PRDRVW = Products.objects.filter(slug=slug)
        coments = productReview.objects.filter(product__in=PRDRVW)
        RCPST = userBlog.objects.order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()

        context = {'shpDetail': shpDetail, 'prd_images': prd_images, 'RCPST': RCPST, 'SMDT': SMDT,
                   'coments': coments}
        return render(request, 'dronzashopDetails.html', context)

    if type == 'services':
        Record = ServicesTypes.objects.get(slug=slug)
        PriceDetail = Pricing.objects.all()
        RCPST = userBlog.objects.order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()
        context = {'rec': Record, 'PRCDT': PriceDetail, 'RCPST': RCPST, 'SMDT': SMDT}
        return render(request, 'serviceDetail.html', context)

    # if type == 'sellDrone':
    #     Record = ServicesTypes.objects.get(sNo=id)
    #     PriceDetail = Pricing.objects.all()
    #     RCPST = userBlog.objects.order_by('-sNo')[:2]
    #     SMDT = SocialMedia.objects.all()
    #     context = {'rec': Record, 'PRCDT': PriceDetail, 'RCPST': RCPST, 'SMDT': SMDT}
    #     return render(request, 'serviceDetail.html', context)

    if type == 'experts':
        Record = OurTeam.objects.get(slug=slug)
        RCPST = userBlog.objects.order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()
        context = {'rec': Record, 'RCPST': RCPST, 'SMDT': SMDT}
        return render(request, 'teamDetail.html', context)

    if type == 'sellDrones':
        Record = sellYourDrone.objects.get(slug=slug)
        product_images = sellYourDroneImages.objects.filter(Product_ID_id=Record.id)
        RCPST = userBlog.objects.order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()
        context = {'rec': Record, 'product_images': product_images, 'RCPST': RCPST, 'SMDT': SMDT}
        return render(request, 'sellDrone_Detail.html', context)

    if type == 'orders':
        Record = Place_Order.objects.get(uuid=slug)
        p_id = Record.product_id.split(",")
        product_data = Products.objects.filter(id__in=p_id).values('name', 'image')

        price_total = Record.p_total.split(",")
        p_quantity = Record.p_quantity.split(",")
        p_price = Record.p_price.split(",")
        RCPST = userBlog.objects.order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()
        context = {'Record': Record, 'price_total': price_total, 'p_quantity': p_quantity, 'p_price': p_price,
                   'product_data': product_data, 'RCPST': RCPST, 'SMDT': SMDT}
        if request.method == 'POST':
            Record.status = request.POST.get('status')
            Record.save()
            return redirect('/orders')

        return render(request, 'order_detail.html', context)

    if type == 'track_order':
        Record = Place_Order.objects.get(uuid=slug)
        p_id = Record.product_id.split(",")
        product_data = Products.objects.filter(id__in=p_id).values('name', 'image')

        price_total = Record.p_total.split(",")
        p_quantity = Record.p_quantity.split(",")
        p_price = Record.p_price.split(",")
        RCPST = userBlog.objects.order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()

        context = {'Record': Record, 'price_total': price_total, 'p_quantity': p_quantity, 'p_price': p_price,
                   'product_data': product_data, 'RCPST': RCPST, 'SMDT': SMDT}
        return render(request, 'track_order_detail.html', context)
