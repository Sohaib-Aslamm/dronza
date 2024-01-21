from django.shortcuts import render, redirect
from dronzaPanel.models import ServicesTypes, Pricing, OurTeam, SocialMedia, userBlog, MainSlider
from home.models import sellYourDrone, sellYourDroneImages
from django.contrib.auth.models import User
from django.core.paginator import Paginator


def DetailRecord(request, type, slug):
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
        product_images = sellYourDroneImages.objects.filter(Product=Record)
        RCPST = userBlog.objects.order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()
        SLIDER = MainSlider.objects.filter(page='sell_drones_detail_page')
        SEOTAGS = [{'title': Record.title, 'description': Record.description[:160], 'tags': Record.title,
                    'canonical_link': f'https://dronza.org/sell-drones/{Record.slug}'}]

        context = {'rec': Record, 'product_images': product_images, 'RCPST': RCPST, 'SMDT': SMDT, 'SEOTAGS': SEOTAGS,
                   'SLIDER': SLIDER}
        return render(request, 'sellDrone_Detail.html', context)
