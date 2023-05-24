from django.shortcuts import render
from dronzaPanel.models import ServicesTypes, Pricing, SocialMedia, userBlog


def services(request):
    RegularServices = ServicesTypes.objects.filter(type='RegularService')
    MAINSERVICES = ServicesTypes.objects.filter(type='MainService')
    PRCDT = Pricing.objects.all()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    latest_keywords = userBlog.objects.order_by('-sNo').values_list('tags', flat=True)[:3]
    context = {'RegularServices': RegularServices, 'PRCDT': PRCDT, 'RCPST': RCPST, 'SMDT': SMDT,
               'MAINSERVICES': MAINSERVICES, 'latest_keywords': latest_keywords}
    return render(request, 'Services.html', context)