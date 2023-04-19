from django.shortcuts import render
from home.models import userBlog
from dronzaPanel.models import SocialMedia


def thankyou(request):
    return render(request, 'thanks.html')


def orderDone(request):
    return render(request, 'Order_Done.html')


def error404(request):
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    context = {'RCPST': RCPST, 'SMDT': SMDT}
    return render(request, 'error404.html', context)