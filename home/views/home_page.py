from django.shortcuts import render, redirect

from dronzaPanel.models import OurTeam, userBlog, SocialMedia, MainSlider, HomeHIW, HomeHTU, HomeAbout, HomeSRFP, \
    VideoGallery, WhatPeopleSay, OurPartner, seoTags
from home.commands import Data_Logger
from home.enumerators import SOLD_STATUS, DJANGO_VIEWS
from home.models import sellYourDrone


# Create your views here.


def baseTemplate(request):

    context = {
        'recent_blog_post': userBlog.objects.order_by('-sNo')[:2],
        'social_media': SocialMedia.objects.all(),
    }
    return render(request, 'baseHome.html', context)


def index(request):
    try:
        context = {
            'how_it_work': HomeHIW.objects.all(),
            'how_to_use': HomeHTU.objects.all(),
            'about': HomeAbout.objects.all(),
            'satisfied_clients': HomeSRFP.objects.all(),
            'video_gallery': VideoGallery.objects.all(),
            'our_team': OurTeam.objects.all(),
            'testimonials': WhatPeopleSay.objects.all(),
            'our_partner': OurPartner.objects.all(),
            'blog_post': userBlog.objects.order_by('sNo')[:3],
            'recent_blog_post': userBlog.objects.order_by('-sNo')[:2],
            'social_media': SocialMedia.objects.all(),
            'seo_tags': seoTags.objects.filter(page='home_page'),
            'featured_products': sellYourDrone.objects.filter(is_featured=True, status=SOLD_STATUS.AVAILABLE),
        }
        return render(request, 'Home.html', context)
    except Exception as e:
        Data_Logger.log_error_message(DJANGO_VIEWS.HOME_PAGE, e, Data_Logger.get_client_ip(request))
        return redirect('bad-request')
