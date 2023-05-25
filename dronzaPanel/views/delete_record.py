from dronzaPanel.models import AboutTitlePost, QualityTrust, OurTeam, ServicesTypes, Pricing, Gallery, userBlog, \
    SocialMedia, MainSlider, HomeHIW, HomeHTU, HomeAbout, Products, HomeSRFP, VideoGallery, WhatPeopleSay, OurPartner

from django.contrib.auth.models import User


from home.models import contact_us, Place_Order, blog_Review

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from dronzaPanel.decorators import admin_only

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Delete Functions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


@login_required(login_url='/user_login')
@admin_only
def MasterDelete(request, type):
    if type == 'Message':
        MasterDeleter = contact_us.objects.all()
        MasterDeleter.delete()
        return redirect('/admin')


@login_required(login_url='/user_login')
@admin_only
def Delete(request, id, type):
    model_mapping = {
        'User': (User, '/UserList'),
        'adminabout': (AboutTitlePost, '/adminabout'),
        'adminqualityTrust': (QualityTrust, '/adminqualityTrust'),
        'team': (OurTeam, '/adminTeam'),
        'servicesType': (ServicesTypes, '/adminservicesType'),
        'pricing': (Pricing, '/adminpricing'),
        'gallery': (Gallery, '/admingallery'),
        'blog': (userBlog, '/adminblog'),
        'socialMedia': (SocialMedia, '/adminsocialmedia'),
        'Messages': (contact_us, '/admin'),
        'HomeSlider': (MainSlider, '/adminHomeSlider'),
        'HowItWork': (HomeHIW, '/adminHowItWork'),
        'HowToUse': (HomeHTU, '/adminHowToUse'),
        'HomeAbout': (HomeAbout, '/adminHomeAbout'),
        'Products': (Products, '/adminDroneProducts'),
        'SRFP': (HomeSRFP, '/adminHomeSRFP'),
        'VideoGallery': (VideoGallery, '/adminVideoGallery'),
        'PeopleSay': (WhatPeopleSay, '/adminPeopleSay'),
        'OurPartner': (OurPartner, '/adminOurPartner'),
        'deleteOrder': (Place_Order, '/orders'),
        'user_comment': (blog_Review, '/user_comments'),
    }

    if type in model_mapping:
        model, redirect_url = model_mapping[type]
        try:
            delete_record = model.objects.get(id=id)
            delete_record.delete()
        except model.DoesNotExist:
            pass
        return redirect(redirect_url)
    else:
        return redirect('/admin')
