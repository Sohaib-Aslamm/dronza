from django.shortcuts import render, redirect
from dronzaPanel.models import Products, ServicesTypes, Pricing, OurTeam, SocialMedia, userBlog, productImages, \
    MainSlider
from home.models import Place_Order, sellYourDrone, sellYourDroneImages, productReview
from django.contrib.auth.models import User
from django.core.paginator import Paginator


def DetailRecord(request, type, slug):
    if type == 'UserList':
        Record = User.objects.get(username=slug)
        context = {'Record': Record}
        return render(request, 'user_detail.html', context)

    if type == 'sellerProductsList':
        Record = sellYourDrone.objects.filter(user_id=slug).order_by('-id')
        User_Record = User.objects.get(id=slug)
        paginator = Paginator(Record, 10)
        pageNo = request.GET.get('page')
        all_Records = paginator.get_page(pageNo)
        totalPages = paginator.num_pages
        pageList = range(1, totalPages + 1)
        context = {'Record': all_Records, 'User_Record': User_Record, 'lastPage': totalPages, 'pageList': pageList}
        return render(request, 'admin_view_seller_product_list.html', context)

    if type == 'shop':
        shpDetail = Products.objects.get(slug=slug)
        prd_images = productImages.objects.filter(Product_ID_id=shpDetail.id)
        PRDRVW = Products.objects.filter(slug=slug)
        coments = productReview.objects.filter(product__in=PRDRVW)
        RCPST = userBlog.objects.order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()
        SLIDER = MainSlider.objects.filter(page='shop_detail_page')
        SEOTAGS = [{'title': shpDetail.name, 'description': shpDetail.description[:160], 'tags': shpDetail.tags,
                    'canonical_link': f'https://dronza.org/shop/{shpDetail.slug}'}]

        context = {'shpDetail': shpDetail, 'prd_images': prd_images, 'RCPST': RCPST, 'SMDT': SMDT,
                   'coments': coments, 'SEOTAGS': SEOTAGS, 'SLIDER': SLIDER}
        return render(request, 'dronzashopDetails.html', context)

    if type == 'services':
        Record = ServicesTypes.objects.get(slug=slug)
        PriceDetail = Pricing.objects.all()
        RCPST = userBlog.objects.order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()
        SLIDER = MainSlider.objects.filter(page='services_detail_page')
        SEOTAGS = [{'title': Record.title, 'description': Record.Description[:160], 'tags': Record.title,
                    'canonical_link': f'https://dronza.org/services/{Record.slug}'}]

        context = {'rec': Record, 'PRCDT': PriceDetail, 'RCPST': RCPST, 'SMDT': SMDT, 'SEOTAGS': SEOTAGS,
                   'SLIDER': SLIDER}
        return render(request, 'serviceDetail.html', context)

    if type == 'experts':
        Record = OurTeam.objects.get(slug=slug)
        RCPST = userBlog.objects.order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()
        SLIDER = MainSlider.objects.filter(page='experts_detail_page')
        SEOTAGS = [{'title': Record.name, 'description': Record.description[:160], 'tags': Record.name,
                    'canonical_link': f'https://dronza.org/experts/{Record.slug}'}]

        context = {'rec': Record, 'RCPST': RCPST, 'SMDT': SMDT, 'SEOTAGS': SEOTAGS, 'SLIDER': SLIDER}
        return render(request, 'teamDetail.html', context)

    if type == 'sell-drones':
        Record = sellYourDrone.objects.get(slug=slug)
        product_images = sellYourDroneImages.objects.filter(Product_ID_id=Record.id)
        RCPST = userBlog.objects.order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()
        SLIDER = MainSlider.objects.filter(page='sell_drones_detail_page')
        SEOTAGS = [{'title': Record.title, 'description': Record.description[:160], 'tags': Record.title,
                    'canonical_link': f'https://dronza.org/sellDrones/{Record.slug}'}]

        context = {'rec': Record, 'product_images': product_images, 'RCPST': RCPST, 'SMDT': SMDT, 'SEOTAGS': SEOTAGS,
                   'SLIDER': SLIDER}
        return render(request, 'sellDrone_Detail.html', context)

    if type == 'orders':
        Record = Place_Order.objects.get(uuid=slug)
        p_id = Record.product_id.split(",")
        product_data = Products.objects.filter(id__in=p_id)

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

    if type == 'track-order':
        Record = Place_Order.objects.get(uuid=slug)
        p_id = Record.product_id.split(",")
        product_data = Products.objects.filter(id__in=p_id)

        price_total = Record.p_total.split(",")
        p_quantity = Record.p_quantity.split(",")
        p_price = Record.p_price.split(",")
        RCPST = userBlog.objects.order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()
        SLIDER = MainSlider.objects.filter(page='order_detail_page')

        SEOTAGS = [{'title': 'DronZa: Customer order detail', 'description': 'Track your order on DronZa to stay updated on the status of your drone purchase. Enter your order details and get real-time tracking information and estimated delivery time.',
                    'tags': 'DronZa: Customer order detail', 'canonical_link': f'https://dronza.org/track_order/{Record.uuid}'}]

        context = {'Record': Record, 'price_total': price_total, 'p_quantity': p_quantity, 'p_price': p_price,
                   'product_data': product_data, 'RCPST': RCPST, 'SMDT': SMDT, 'SEOTAGS': SEOTAGS, 'SLIDER': SLIDER}
        return render(request, 'track_order_detail.html', context)
