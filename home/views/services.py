from django.shortcuts import render

from dronzaPanel.enumeratorts import ServicesType
from dronzaPanel.models import ServicesTypes, Pricing, SocialMedia, userBlog, seoTags, MainSlider


def services(request):

    context = {
        'RegularServices': ServicesTypes.objects.filter(type=ServicesType.REGULAR_SERVICE),
        'PRCDT': Pricing.objects.all(),
        'RCPST': userBlog.objects.order_by('-sNo')[:2],
        'SMDT': SocialMedia.objects.all(),
        'MAINSERVICES': ServicesTypes.objects.filter(type=ServicesType.MAIN_SERVICE),
        'SEOTAGS': seoTags.objects.filter(page='services_page'),
        'SLIDER': MainSlider.objects.filter(page='services_page')
    }

    return render(request, 'Services.html', context)
