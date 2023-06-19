from django.shortcuts import render
from home.models import userBlog
from dronzaPanel.models import SocialMedia, seoTags, MainSlider


def thankyou(request):
    return render(request, 'thanks.html')


def orderDone(request):
    return render(request, 'Order_Done.html')


def coming_soon(request):
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    SEOTAGS = seoTags.objects.filter(page='coming_soon')
    SLIDER = MainSlider.objects.filter(page='coming_soon_page')
    context = {
        'RCPST': RCPST,
        'SMDT': SMDT,
        'SEOTAGS': SEOTAGS,
        'SLIDER': SLIDER,
    }
    return render(request, 'error404.html', context)
