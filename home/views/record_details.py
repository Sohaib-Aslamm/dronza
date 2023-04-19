from django.shortcuts import render, redirect
from dronzaPanel.models import Products, ServicesTypes, Pricing, OurTeam, SocialMedia, userBlog
from home.models import Place_Order, sellYourDrone, sellYourDroneImages
from django.contrib.auth.models import User


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


def RecordbyUUID(request, id, uuid, type):
    if type == 'sellerProduct':
        Record = sellYourDrone.objects.get(uuid=uuid)
        product_images = sellYourDroneImages.objects.filter(Product_ID_id=id)
        RCPST = userBlog.objects.all().order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()
        context = {'rec': Record, 'product_images': product_images, 'RCPST': RCPST, 'SMDT': SMDT}
        return render(request, 'sellDrone_Detail.html', context)

    if type == 'track_order':
        Record = Place_Order.objects.get(id=id, uuid=uuid)
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