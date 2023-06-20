from dronzaPanel.models import AboutTitlePost, QualityTrust, OurTeam, ServicesTypes, Pricing, Gallery, userBlog, \
    SocialMedia, MainSlider, HomeHIW, HomeHTU, HomeAbout, Products, HomeSRFP, VideoGallery, WhatPeopleSay, OurPartner, \
    seoTags, EmailContent

from django.contrib.auth.models import User


from home.models import contact_us, Place_Order, blog_Review

from django.shortcuts import redirect

from dronzaPanel.decorators import admin_only, custom_login_required

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Delete Functions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


@custom_login_required
@admin_only
def MasterDelete(request, type):
    if type == 'Message':
        MasterDeleter = contact_us.objects.all()
        MasterDeleter.delete()
        return redirect('/admin')


@custom_login_required
@admin_only
def Delete(request, id, type):
    if type == 'User':
        DeleteRecord = User.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/UserList')

    if type == 'adminabout':
        DeleteRecord = AboutTitlePost.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/adminabout')

    if type == 'adminqualityTrust':
        DeleteRecord = QualityTrust.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/adminqualityTrust')

    if type == 'team':
        DeleteRecord = OurTeam.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/adminTeam')

    if type == 'servicesType':
        DeleteRecord = ServicesTypes.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/adminservicesType')

    if type == 'pricing':
        DeleteRecord = Pricing.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/adminpricing')

    if type == 'gallery':
        DeleteRecord = Gallery.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/admingallery')

    if type == 'blog':
        DeleteRecord = userBlog.objects.get(sNo=id)
        DeleteRecord.delete()
        return redirect('/adminblog')

    if type == 'socialMedia':
        DeleteRecord = SocialMedia.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/adminsocialmedia')

    if type == 'Messages':
        DeleteRecord = contact_us.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/admin')

    if type == 'HomeSlider':
        DeleteRecord = MainSlider.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/adminHomeSlider')

    if type == 'HowItWork':
        DeleteRecord = HomeHIW.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/adminHowItWork')

    if type == 'HowToUse':
        DeleteRecord = HomeHTU.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/adminHowToUse')

    if type == 'HomeAbout':
        DeleteRecord = HomeAbout.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/adminHomeAbout')

    if type == 'Products':
        DeleteRecord = Products.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/adminDroneProducts')

    # if type == 'droneParts':
    #     DeleteRecord = droneParts.objects.get(id=id)
    #     DeleteRecord.delete()
    #     return redirect('/adminDroneParts')

    if type == 'SRFP':
        DeleteRecord = HomeSRFP.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/adminHomeSRFP')

    if type == 'VideoGallery':
        DeleteRecord = VideoGallery.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/adminVideoGallery')

    if type == 'PeopleSay':
        DeleteRecord = WhatPeopleSay.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/adminPeopleSay')

    if type == 'OurPartner':
        DeleteRecord = OurPartner.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/adminOurPartner')

    if type == 'deleteOrder':
        DeleteRecord = Place_Order.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/orders')

    if type == 'user_comment':
        DeleteRecord = blog_Review.objects.get(sNo=id)
        DeleteRecord.delete()
        return redirect('/user_comments')

    if type == 'seoTags':
        DeleteRecord = seoTags.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/seotags')

    if type == 'email_content':
        DeleteRecord = EmailContent.objects.get(id=id)
        DeleteRecord.delete()
        return redirect('/admin-email-content')
