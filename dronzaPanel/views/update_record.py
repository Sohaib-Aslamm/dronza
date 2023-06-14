from dronzaPanel.forms import AboutTitlePostForm, QualityTrustForm, OurTeamForm, ServicesTypeForm, PricingForm, \
     GalleryForm, SocialMediaForm, MainSliderForm, HomeHIWForm, HomeHTUForm, HomeAboutForm, \
     HomeSRFPForm, VideoGalleryForm, WhatPeopleSForm, OurPartnerForm, SEOTagsForm

from dronzaPanel.models import AboutTitlePost, QualityTrust, OurTeam, ServicesTypes, Pricing, Gallery, userBlog, \
    SocialMedia, MainSlider, HomeHIW, HomeHTU, HomeAbout, Products, HomeSRFP, VideoGallery, WhatPeopleSay, OurPartner, \
    seoTags

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Update Functions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


@login_required(login_url='/user-login')
def Update(request, id, type):
    if type == 'adminabout':
        if request.method == 'POST':
            UpdateRecord = AboutTitlePost.objects.get(id=id)
            UpdateForm = AboutTitlePostForm(request.POST, request.FILES, instance=UpdateRecord)
            if UpdateForm.is_valid():
                UpdateForm.save()
                return redirect('/adminabout')
        else:
            UpdateRecord = AboutTitlePost.objects.get(id=id)
            UpdateForm = AboutTitlePostForm(instance=UpdateRecord)
        return render(request, 'Update/updateAboutTitlePost.html', {'form': UpdateForm})

    if type == 'adminqualityTrust':
        if request.method == 'POST':
            UpdateRecord = QualityTrust.objects.get(id=id)
            UpdateForm = QualityTrustForm(request.POST, request.FILES, instance=UpdateRecord)
            if UpdateForm.is_valid():
                UpdateForm.save()
                return redirect('/adminqualityTrust')
        else:
            UpdateRecord = QualityTrust.objects.get(id=id)
            UpdateForm = QualityTrustForm(instance=UpdateRecord)
        return render(request, 'Update/updateQualityTrust.html', {'form': UpdateForm})

    if type == 'team':
        if request.method == 'POST':
            UpdateRecord = OurTeam.objects.get(id=id)
            UpdateForm: OurTeamForm = OurTeamForm(request.POST, request.FILES, instance=UpdateRecord)
            if UpdateForm.is_valid():
                UpdateForm.save()
                return redirect('/adminTeam')
        else:
            UpdateRecord = OurTeam.objects.get(id=id)
            UpdateForm = OurTeamForm(instance=UpdateRecord)
        return render(request, 'Update/updateOurTeam.html', {'form': UpdateForm})

    if type == 'servicesType':
        if request.method == 'POST':
            UpdateRecord = ServicesTypes.objects.get(id=id)
            UpdateForm = ServicesTypeForm(request.POST, request.FILES, instance=UpdateRecord)
            if UpdateForm.is_valid():
                UpdateForm.save()
                return redirect('/adminservicesType')
        else:
            UpdateRecord = ServicesTypes.objects.get(id=id)
            UpdateForm = ServicesTypeForm(instance=UpdateRecord)
        return render(request, 'Update/updateServicesType.html', {'form': UpdateForm})

    if type == 'pricing':
        if request.method == 'POST':
            UpdateRecord = Pricing.objects.get(id=id)
            UpdateForm = PricingForm(request.POST, request.FILES, instance=UpdateRecord)
            if UpdateForm.is_valid():
                UpdateForm.save()
                return redirect('/adminpricing')
        else:
            UpdateRecord = Pricing.objects.get(id=id)
            UpdateForm = PricingForm(instance=UpdateRecord)
        return render(request, 'Update/updatePricing.html', {'form': UpdateForm})

    if type == 'gallery':
        if request.method == 'POST':
            UpdateRecord = Gallery.objects.get(id=id)
            UpdateForm = GalleryForm(request.POST, request.FILES, instance=UpdateRecord)
            if UpdateForm.is_valid():
                UpdateForm.save()
                return redirect('/admingallery')
        else:
            UpdateRecord = Gallery.objects.get(id=id)
            UpdateForm = GalleryForm(instance=UpdateRecord)
        return render(request, 'Update/updateGallery.html', {'form': UpdateForm})

    if type == 'blog':

        UpdateForm = userBlog.objects.get(sNo=id)
        if request.method == 'POST':
            file_data = request.POST.get('edit_file')
            UpdateForm.title = request.POST.get('title')
            UpdateForm.heading = request.POST.get('heading')
            UpdateForm.tags = request.POST.get('tags')
            UpdateForm.quote = request.POST.get('quote')
            UpdateForm.quote_by = request.POST.get('quote_by')
            UpdateForm.description = request.POST.get('editor1')
            if not file_data == 'False':
                UpdateForm.Icon = request.FILES['icon']
            UpdateForm.save()
            return redirect('/adminblog')

        return render(request, 'Update/updateBlog.html', {'form': UpdateForm})

    if type == 'socialMedia':
        if request.method == 'POST':
            UpdateRecord = SocialMedia.objects.get(id=id)
            UpdateForm = SocialMediaForm(request.POST, request.FILES, instance=UpdateRecord)
            if UpdateForm.is_valid():
                UpdateForm.save()
                return redirect('/adminsocialmedia')
        else:
            UpdateRecord = SocialMedia.objects.get(id=id)
            UpdateForm = SocialMediaForm(instance=UpdateRecord)
        return render(request, 'Update/updateSocialMedia.html', {'form': UpdateForm})

    if type == 'HomeSlider':
        if request.method == 'POST':
            UpdateRecord = MainSlider.objects.get(id=id)
            UpdateForm = MainSliderForm(request.POST, request.FILES, instance=UpdateRecord)
            if UpdateForm.is_valid():
                UpdateForm.save()
                return redirect('/adminHomeSlider')
        else:
            UpdateRecord = MainSlider.objects.get(id=id)
            UpdateForm = MainSliderForm(instance=UpdateRecord)
        return render(request, 'Update/updateHomeSlider.html', {'form': UpdateForm})

    if type == 'HowItWork':
        if request.method == 'POST':
            UpdateRecord = HomeHIW.objects.get(id=id)
            UpdateForm = HomeHIWForm(request.POST, request.FILES, instance=UpdateRecord)
            if UpdateForm.is_valid():
                UpdateForm.save()
                return redirect('/adminHowItWork')
        else:
            UpdateRecord = HomeHIW.objects.get(id=id)
            UpdateForm = HomeHIWForm(instance=UpdateRecord)
        return render(request, 'Update/updateHowItWork.html', {'form': UpdateForm})

    if type == 'HowToUse':
        if request.method == 'POST':
            UpdateRecord = HomeHTU.objects.get(id=id)
            UpdateForm = HomeHTUForm(request.POST, request.FILES, instance=UpdateRecord)
            if UpdateForm.is_valid():
                UpdateForm.save()
                return redirect('/adminHowToUse')
        else:
            UpdateRecord = HomeHTU.objects.get(id=id)
            UpdateForm = HomeHTUForm(instance=UpdateRecord)
        return render(request, 'Update/updateHowToUse.html', {'form': UpdateForm})

    if type == 'HomeAbout':
        if request.method == 'POST':
            UpdateRecord = HomeAbout.objects.get(id=id)
            UpdateForm = HomeAboutForm(request.POST, request.FILES, instance=UpdateRecord)
            if UpdateForm.is_valid():
                UpdateForm.save()
                return redirect('/adminHowToUse')
        else:
            UpdateRecord = HomeAbout.objects.get(id=id)
            UpdateForm = HomeAboutForm(instance=UpdateRecord)
        return render(request, 'Update/updateHomeAbout.html', {'form': UpdateForm})

    if type == 'Products':
        UpdateRecord = Products.objects.get(id=id)
        if request.method == 'POST':
           UpdateRecord.name = request.POST.get('name')
           UpdateRecord.cPrice = request.POST.get('cPrice')
           UpdateRecord.price = request.POST.get('price')
           UpdateRecord.currency = request.POST.get('currency')
           UpdateRecord.availability = request.POST.get('availability')
           UpdateRecord.color = request.POST.get('color')
           UpdateRecord.featured = request.POST.get('featured')
           UpdateRecord.category = request.POST.get('category')
           UpdateRecord.tags = request.POST.get('tags')
           UpdateRecord.label1 = request.POST.get('label1')
           UpdateRecord.label2 = request.POST.get('label2')
           UpdateRecord.label3 = request.POST.get('label3')
           UpdateRecord.label4 = request.POST.get('label4')
           UpdateRecord.label5 = request.POST.get('label5')
           UpdateRecord.label6 = request.POST.get('label6')
           UpdateRecord.label7 = request.POST.get('label7')
           UpdateRecord.label8 = request.POST.get('label8')
           UpdateRecord.input1 = request.POST.get('input1')
           UpdateRecord.input2 = request.POST.get('input2')
           UpdateRecord.input3 = request.POST.get('input3')
           UpdateRecord.input4 = request.POST.get('input4')
           UpdateRecord.input5 = request.POST.get('input5')
           UpdateRecord.input6 = request.POST.get('input6')
           UpdateRecord.input7 = request.POST.get('input7')
           UpdateRecord.input8 = request.POST.get('input8')
           UpdateRecord.description = request.POST.get('description')
           UpdateRecord.description = request.POST.get('editor1')

           file_data = request.POST.get('edit_file')
           if not file_data == 'False':
               UpdateRecord.image = request.FILES['image']

           UpdateRecord.save()
           return redirect('/adminDroneProducts')

        context = {'Record': UpdateRecord}
        return render(request, 'Update/updateDroneProducts.html', context)

    # if type == 'droneParts':
    #     if request.method == 'POST':
    #         UpdateRecord = droneParts.objects.get(id=id)
    #         UpdateForm = dronePartsForm(request.POST, request.FILES, instance=UpdateRecord)
    #         if UpdateForm.is_valid():
    #             UpdateForm.save()
    #             return redirect('/adminDroneParts')
    #     else:
    #         UpdateRecord = droneParts.objects.get(id=id)
    #         UpdateForm = dronePartsForm(instance=UpdateRecord)
    #     return render(request, 'Update/updateDroneParts.html', {'form': UpdateForm})

    if type == 'SRFP':
        if request.method == 'POST':
            UpdateRecord = HomeSRFP.objects.get(id=id)
            UpdateForm = HomeSRFPForm(request.POST, request.FILES, instance=UpdateRecord)
            if UpdateForm.is_valid():
                UpdateForm.save()
                return redirect('/adminHomeSRFP')
        else:
            UpdateRecord = HomeSRFP.objects.get(id=id)
            UpdateForm = HomeSRFPForm(instance=UpdateRecord)
        return render(request, 'Update/updateHomeSRFP.html', {'form': UpdateForm})

    if type == 'VideoGallery':
        if request.method == 'POST':
            UpdateRecord = VideoGallery.objects.get(id=id)
            UpdateForm = VideoGalleryForm(request.POST, request.FILES, instance=UpdateRecord)
            if UpdateForm.is_valid():
                UpdateForm.save()
                return redirect('/adminVideoGallery')
        else:
            UpdateRecord = VideoGallery.objects.get(id=id)
            UpdateForm = VideoGalleryForm(instance=UpdateRecord)
        return render(request, 'Update/updateHomeVideoGallery.html', {'form': UpdateForm})

    if type == 'PeopleSay':
        if request.method == 'POST':
            UpdateRecord = WhatPeopleSay.objects.get(id=id)
            UpdateForm = WhatPeopleSForm(request.POST, request.FILES, instance=UpdateRecord)
            if UpdateForm.is_valid():
                UpdateForm.save()
                return redirect('/adminPeopleSay')
        else:
            UpdateRecord = WhatPeopleSay.objects.get(id=id)
            UpdateForm = WhatPeopleSForm(instance=UpdateRecord)
        return render(request, 'Update/updatePeopleSay.html', {'form': UpdateForm})

    if type == 'OurPartner':
        if request.method == 'POST':
            UpdateRecord = OurPartner.objects.get(id=id)
            UpdateForm = OurPartnerForm(request.POST, request.FILES, instance=UpdateRecord)
            if UpdateForm.is_valid():
                UpdateForm.save()
                return redirect('/adminOurPartner')
        else:
            UpdateRecord = OurPartner.objects.get(id=id)
            UpdateForm = OurPartnerForm(instance=UpdateRecord)
        return render(request, 'Update/updateOurPartner.html', {'form': UpdateForm})

    if type == 'seoTags':
        if request.method == 'POST':
            UpdateRecord = seoTags.objects.get(id=id)
            UpdateForm = SEOTagsForm(request.POST, request.FILES, instance=UpdateRecord)
            if UpdateForm.is_valid():
                UpdateForm.save()
                return redirect('/seotags')
        else:
            UpdateRecord = seoTags.objects.get(id=id)
            UpdateForm = SEOTagsForm(instance=UpdateRecord)
        return render(request, 'Update/UpdateSEOTags.html', {'form': UpdateForm})
