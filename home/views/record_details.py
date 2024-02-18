from django.shortcuts import render, redirect
from dronzaPanel.models import ServicesTypes, Pricing, OurTeam, SocialMedia, userBlog, MainSlider
from home.commands import Data_Logger
from home.enumerators import DRONE_CONDITION, STAR_MAP, DJANGO_VIEWS
from home.models import sellYourDrone, sellYourDroneImages


def get_instance_detail(request, record_type, slug):
    try:
        if record_type == 'services':
            instance = ServicesTypes.objects.get(slug=slug)
            seo_tags = [{'title': instance.title,
                         'description': f'Explore our latest service: {instance.title}',
                         'tags': instance.title,
                        'canonical_link': f'https://dronza.org/services/{instance.slug}'}]

            context = {
                'rec': instance,
                'price_detail': Pricing.objects.all(),
                'recent_blog_post': userBlog.objects.order_by('-sNo')[:2],
                'social_media': SocialMedia.objects.all(),
                'seo_tags': seo_tags,
                'SLIDER': MainSlider.objects.filter(page='services_detail_page'),
            }
            return render(request, 'serviceDetail.html', context)

        if record_type == 'experts':
            instance = OurTeam.objects.get(slug=slug)
            seo_tags = [{'title': instance.name,
                         'description': f'View our expert: {instance.name}',
                         'tags': instance.name,
                         'canonical_link': f'https://dronza.org/experts/{instance.slug}'}]

            context = {
                'rec': instance,
                'recent_blog_post': userBlog.objects.order_by('-sNo')[:2],
                'social_media': SocialMedia.objects.all(),
                'seo_tags': seo_tags,
                'SLIDER': MainSlider.objects.filter(page='experts_detail_page'),
            }
            return render(request, 'teamDetail.html', context)

        if record_type == 'sell-drones':
            instance = sellYourDrone.objects.get(slug=slug)
            seo_tags = [{'title': instance.title,
                         'description': f'Explore this customer listing: {instance.title}',
                         'tags': instance.title,
                         'canonical_link': f'https://dronza.org/sell-drones/{instance.slug}'}]

            context = {
                'rec': instance,
                'product_images': sellYourDroneImages.objects.filter(Product=instance),
                'recent_blog_post': userBlog.objects.order_by('-sNo')[:2],
                'social_media': SocialMedia.objects.all(),
                'seo_tags': seo_tags,
                'SLIDER': MainSlider.objects.filter(page='sell_drones_detail_page'),
                'condition': DRONE_CONDITION.choices,
                'filled_stars': range(STAR_MAP.star_map.get(instance.condition, 0)),
                'empty_stars': range(5 - STAR_MAP.star_map.get(instance.condition, 0)),
            }
            return render(request, 'sellDrone_Detail.html', context)
    except Exception as e:
        Data_Logger.log_error_message(DJANGO_VIEWS.RECORD_DETAILS, e, Data_Logger.get_client_ip(request))
        return redirect('error-404')
