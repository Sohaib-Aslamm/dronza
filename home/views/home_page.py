from django.shortcuts import render

from dronzaPanel.models import OurTeam, userBlog, SocialMedia, MainSlider, HomeHIW, HomeHTU, HomeAbout, HomeSRFP, \
    VideoGallery, WhatPeopleSay, OurPartner, seoTags
from home.enumerators import SOLD_STATUS
from home.models import sellYourDrone


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
    featured_products = sellYourDrone.objects.filter(is_featured=True, status=SOLD_STATUS.AVAILABLE)
    SRFP = HomeSRFP.objects.all()
    HVG = VideoGallery.objects.all()
    OURTM = OurTeam.objects.all()
    WPSDT = WhatPeopleSay.objects.all()
    OPTDT = OurPartner.objects.all()
    UBDT = userBlog.objects.order_by('sNo')[:3]
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    SEOTAGS = seoTags.objects.filter(page='home_page')
    context = {'MSLDR': MSLDR, 'HIWork': HIWork, 'HTUSE': HTUSE, 'HABT': HABT, 'featured_products': featured_products, 'SRFP': SRFP, 'HVG': HVG,
               'OURTM': OURTM, 'WPSDT': WPSDT, 'OPTDT': OPTDT, 'UBDT': UBDT, 'RCPST': RCPST, 'SMDT': SMDT,
               'SEOTAGS': SEOTAGS}
    return render(request, 'Home.html', context)
