from django.shortcuts import render, redirect

from dronzaPanel.enumeratorts import ServicesType
from dronzaPanel.models import ServicesTypes, Pricing, SocialMedia, userBlog, seoTags, MainSlider
from home.commands import Data_Logger
from home.enumerators import DJANGO_VIEWS


def services(request):
    try:
        context = {
            'RegularServices': ServicesTypes.objects.filter(type=ServicesType.REGULAR_SERVICE),
            'pricing_table': Pricing.objects.all(),
            'recent_blog_post': userBlog.objects.order_by('-sNo')[:2],
            'social_media': SocialMedia.objects.all(),
            'seo_tags': seoTags.objects.filter(page='services_page'),
            'MainServices': ServicesTypes.objects.filter(type=ServicesType.MAIN_SERVICE),
            'SLIDER': MainSlider.objects.filter(page='services_page')
        }

        return render(request, 'Services.html', context)
    except Exception as e:
        Data_Logger.log_error_message(DJANGO_VIEWS.SERVICES, e, Data_Logger.get_client_ip(request))
        return redirect('bad-request')

