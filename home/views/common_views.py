from django.shortcuts import render
from home.models import userBlog
from dronzaPanel.models import SocialMedia, seoTags


def thankyou(request):
    return render(request, 'thanks.html')


def orderDone(request):
    return render(request, 'Order_Done.html')


def error404(request):
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    context = {
        'RCPST': RCPST,
        'SMDT': SMDT
    }
    return render(request, 'error404.html', context)
