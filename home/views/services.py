from django.shortcuts import render

from dronzaPanel.enumeratorts import ServicesType
from dronzaPanel.models import ServicesTypes, Pricing, SocialMedia, userBlog, seoTags, MainSlider


def services(request):

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
