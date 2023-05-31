from django.shortcuts import render

from dronzaPanel.models import OurTeam, userBlog, SocialMedia, MainSlider, HomeHIW, HomeHTU, HomeAbout, Products, \
    HomeSRFP, VideoGallery, \
    WhatPeopleSay, OurPartner, seoTags


# Create your views here.


def baseTemplate(request):
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    context = {'SMDT': SMDT, 'RCPST': RCPST}
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
    UBDT = userBlog.objects.order_by('sNo')[:3]
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    SEOTAGS = seoTags.objects.filter(page='home_page')
    context = {'MSLDR': MSLDR, 'HIWork': HIWork, 'HTUSE': HTUSE, 'HABT': HABT, 'PRDCT': PRDCT, 'SRFP': SRFP, 'HVG': HVG,
               'OURTM': OURTM, 'WPSDT': WPSDT, 'OPTDT': OPTDT, 'UBDT': UBDT, 'RCPST': RCPST, 'SMDT': SMDT,
               'SEOTAGS': SEOTAGS}
    return render(request, 'Home.html', context)
