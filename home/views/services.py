from django.shortcuts import render
from dronzaPanel.models import ServicesTypes, Pricing, SocialMedia, userBlog, seoTags


def services(request):
    RegularServices = ServicesTypes.objects.filter(type='RegularService')
    MAINSERVICES = ServicesTypes.objects.filter(type='MainService')
    PRCDT = Pricing.objects.all()
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    SEOTAGS = seoTags.objects.filter('services_page')
    context = {'RegularServices': RegularServices, 'PRCDT': PRCDT, 'RCPST': RCPST, 'SMDT': SMDT,
               'MAINSERVICES': MAINSERVICES, 'SEOTAGS': SEOTAGS}
    return render(request, 'Services.html', context)