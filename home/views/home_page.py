from django.shortcuts import render

from dronzaPanel.models import OurTeam, userBlog, SocialMedia, MainSlider, HomeHIW, HomeHTU, HomeAbout, Products, HomeSRFP, VideoGallery, \
    WhatPeopleSay, OurPartner

# Create your views here.


def baseTemplate(request):
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    latest_keywords = userBlog.objects.order_by('-sNo').values_list('tags', flat=True)[:3]
    context = {'SMDT': SMDT, 'RCPST': RCPST, 'latest_keywords': latest_keywords}
    return render(request, 'baseHome.html', context)


def index(request):
    MSLDR = MainSlider.objects.all()
    HIWork = HomeHIW.objects.all()
    HTUSE = HomeHTU.objects.all()
    HABT = HomeAbout.objects.all()
    PRDCT = Products.objects.filter(featured='Featured')
    SRFP = HomeSRFP.objects.all()
    HVG = VideoGallery.objects.all()
    OURTM = OurTeam.objects.all()
    WPSDT = WhatPeopleSay.objects.all()
    OPTDT = OurPartner.objects.all()
    UBDT = userBlog.objects.all()[:3]
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    latest_keywords = userBlog.objects.order_by('-sNo').values_list('tags', flat=True)[:3]
    context = {'MSLDR': MSLDR, 'HIWork': HIWork, 'HTUSE': HTUSE, 'HABT': HABT, 'PRDCT': PRDCT, 'SRFP': SRFP, 'HVG': HVG,
               'OURTM': OURTM, 'WPSDT': WPSDT, 'OPTDT': OPTDT, 'UBDT': UBDT, 'RCPST': RCPST, 'SMDT': SMDT,
               'latest_keywords': latest_keywords}
    return render(request, 'Home.html', context)
