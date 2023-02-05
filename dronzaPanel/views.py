from dronzaPanel.forms import AboutTitlePostForm, QualityTrustForm, OurTeamForm, ServicesTypeForm, PricingForm, \
    GalleryForm, SocialMediaForm, UserForm, MainSliderForm, HomeHIWForm, HomeHTUForm, HomeAboutForm, \
    HomeSRFPForm, VideoGalleryForm, WhatPeopleSForm, OurPartnerForm
from dronzaPanel.models import AboutTitlePost, QualityTrust, OurTeam, ServicesTypes, Pricing, Gallery, userBlog, \
    SocialMedia, MainSlider, HomeHIW, HomeHTU, HomeAbout, Products, HomeSRFP, VideoGallery, WhatPeopleSay, OurPartner, \
    productImages

from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from home.models import hello
from home.models import contact_us, Place_Order, blog_Review
from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from dronzaPanel.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib import messages
from django.core.paginator import Paginator
from home.definedEmails import *
# Create your views here

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Auth Functions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


@unauthenticated_user
def UserRegister(request):
    if request.method == 'POST':
        URFM = UserForm(request.POST)
        if URFM.is_valid():
            user = URFM.save()
            username = URFM.cleaned_data.get('username')
            email = URFM.cleaned_data.get('email')
            URFM.cleaned_data.get('password')

            group = Group.objects.get(name='Customer')   # assign a default group to customer
            user.groups.add(group)

            messages.success(request, f'Hey !  {username} your account created successfully')
            notify_user_registration(username, email)  # Send email to user he is registered
            return redirect('/user_login')
    else:
        URFM = UserForm()
    return render(request, 'User_Register.html', {'form': URFM})


@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/admin')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('/admin')


@login_required(login_url='/user_login')
@admin_only
def user_list(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'admin_user_list.html', context)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Insert Functions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


@login_required(login_url='/user_login')
@admin_only
def adminHome(request):
    my_messages = contact_us.objects.all()
    return render(request, 'HomeAdmin.html', {'my_messages': my_messages})


@login_required(login_url='/user_login')
@admin_only
def viewMessage(request, id):
    messages_detail = contact_us.objects.get(id=id)
    return render(request, 'viewMessages.html', {'messages_detail': messages_detail})


@login_required(login_url='/user_login')
@admin_only
def adminHomeSlider(request):
    if request.method == 'POST':
        MSFM = MainSliderForm(request.POST, request.FILES)
        if MSFM.is_valid():
            TIT = MSFM.cleaned_data['title']
            HDR = MSFM.cleaned_data['header']
            DESC = MSFM.cleaned_data['description']
            PRC = MSFM.cleaned_data['price']
            IMG = MSFM.cleaned_data['image']
            BKIMG = MSFM.cleaned_data['backImage']
            reg = MainSlider(title=TIT, header=HDR, description=DESC, price=PRC, image=IMG, backImage=BKIMG)
            reg.save()
            MSFM = MainSliderForm()
    else:
        MSFM = MainSliderForm()
    SLDT = MainSlider.objects.all()
    return render(request, 'adminHomeSlider.html', {'SLDT': SLDT, 'form': MSFM})


@login_required(login_url='/user_login')
@admin_only
def adminHowItWork(request):
    if request.method == 'POST':
        HIWFM = HomeHIWForm(request.POST, request.FILES)
        if HIWFM.is_valid():
            TIT = HIWFM.cleaned_data['title']
            DESC = HIWFM.cleaned_data['description']
            IMG = HIWFM.cleaned_data['image']
            reg = HomeHIW(title=TIT, description=DESC, image=IMG)
            reg.save()
            HIWFM = HomeHIWForm()
    else:
        HIWFM = HomeHIWForm()
    HIWDT = HomeHIW.objects.all()
    return render(request, 'adminHomeHowitWork.html', {'HIWDT': HIWDT, 'form': HIWFM})


@login_required(login_url='/user_login')
@admin_only
def adminHowToUse(request):
    if request.method == 'POST':
        HTUFM = HomeHTUForm(request.POST, request.FILES)
        if HTUFM.is_valid():
            TIT = HTUFM.cleaned_data['title']
            DESC = HTUFM.cleaned_data['description']
            ICN = HTUFM.cleaned_data['icon']
            reg = HomeHTU(title=TIT, description=DESC, icon=ICN)
            reg.save()
            HTUFM = HomeHTUForm()
    else:
        HTUFM = HomeHTUForm()
    HTUDT = HomeHTU.objects.all()
    return render(request, 'adminHomeHowToUse.html', {'HTUDT': HTUDT, 'form': HTUFM})


@login_required(login_url='/user_login')
@admin_only
def adminHomeAbout(request):
    if request.method == 'POST':
        HABTFM = HomeAboutForm(request.POST, request.FILES)
        if HABTFM.is_valid():
            TIT = HABTFM.cleaned_data['title']
            FT1 = HABTFM.cleaned_data['feature1']
            FT2 = HABTFM.cleaned_data['feature2']
            FT3 = HABTFM.cleaned_data['feature3']
            DESC = HABTFM.cleaned_data['description']
            ICN = HABTFM.cleaned_data['icon']
            reg = HomeAbout(title=TIT, feature1=FT1, feature2=FT2, feature3=FT3, description=DESC, icon=ICN)
            reg.save()
            HABTFM = HomeAboutForm()
    else:
        HABTFM = HomeAboutForm()
    HABDT = HomeAbout.objects.all()
    return render(request, 'adminHomeAbout.html', {'form': HABTFM, 'HABDT': HABDT})


@login_required(login_url='/user_login')
@admin_only
def adminDroneProducts(request):
    if request.method == 'POST':
        TIT = request.POST.get('name')
        CPR = request.POST.get('cPrice')
        DPR = request.POST.get('price')
        CRNCY =request.POST.get('currency')
        AVLBTY = request.POST.get('availability')
        CTR = request.POST.get('category')
        FTRD = request.POST.get('featured')
        CLR = request.POST.get('color')
        lbl1 = request.POST.get('label1')
        input1 = request.POST.get('input1')
        lbl2 = request.POST.get('label2')
        input2 = request.POST.get('input2')
        lbl3 = request.POST.get('label3')
        input3 = request.POST.get('input3')
        lbl4 = request.POST.get('label4')
        input4 = request.POST.get('input4')
        lbl5 = request.POST.get('label5')
        input5 = request.POST.get('input5')
        lbl6 = request.POST.get('label6')
        input6 = request.POST.get('input6')
        lbl7 = request.POST.get('label7')
        input7 = request.POST.get('input7')
        lbl8 = request.POST.get('label8')
        input8 = request.POST.get('input8')
        ICON = request.FILES.get('image')
        images = request.FILES.getlist('images')
        description = request.POST.get('editor1')
        reg = Products(name=TIT, cPrice=CPR, price=DPR, currency=CRNCY, availability=AVLBTY, color=CLR,
                       category=CTR, featured=FTRD, description=description, label1=lbl1, label2=lbl2,
                       label3=lbl3, label4=lbl4, label5=lbl5, label6=lbl6, label7=lbl7, label8=lbl8, input1=input1,
                       input2=input2, input3=input3, input4=input4, input5=input5, input6=input6, input7=input7,
                       input8=input8, image=ICON)
        reg.save()

        latest_id = Products.objects.latest('id').id

        for f in images:
            products = productImages(images=f, Product_ID_id=latest_id)
            products.save()

    PRDTDT = Products.objects.all().order_by('-id')
    paginator = Paginator(PRDTDT, 10)
    pageNo = request.GET.get('page')
    BLGdataFINAL = paginator.get_page(pageNo)
    totalPages = BLGdataFINAL.paginator.num_pages
    context = {'PRDTDT': BLGdataFINAL, 'lastPage': totalPages, 'pageList': [n + 1 for n in range(totalPages)]}
    return render(request, 'adminDroneProducts.html', context)

#
# @login_required(login_url='/user_login')
# @admin_only
# def admindroneParts(request):
#     if request.method == 'POST':
#         images = request.FILES.getlist('images')
#         PRDTFM = dronePartsForm(request.POST, request.FILES)
#         if PRDTFM.is_valid():
#             NAME = PRDTFM.cleaned_data['name']
#             CPR = PRDTFM.cleaned_data['cPrice']
#             DPR = PRDTFM.cleaned_data['price']
#             AVLBTY = PRDTFM.cleaned_data['availability']
#             FTRD = PRDTFM.cleaned_data['featured']
#             CLR = PRDTFM.cleaned_data['color']
#             CRNCY = PRDTFM.cleaned_data['currency']
#             CTGRY = PRDTFM.cleaned_data['category']
#             label1 = PRDTFM.cleaned_data['label1']
#             input1 = PRDTFM.cleaned_data['input1']
#             label2 = PRDTFM.cleaned_data['label2']
#             input2 = PRDTFM.cleaned_data['input2']
#             label3 = PRDTFM.cleaned_data['label3']
#             input3 = PRDTFM.cleaned_data['input3']
#             label4 = PRDTFM.cleaned_data['label4']
#             input4 = PRDTFM.cleaned_data['input4']
#             label5 = PRDTFM.cleaned_data['label5']
#             input5 = PRDTFM.cleaned_data['input5']
#             label6 = PRDTFM.cleaned_data['label6']
#             input6 = PRDTFM.cleaned_data['input6']
#             DESC = PRDTFM.cleaned_data['description']
#             THMBN = PRDTFM.cleaned_data['image']
#             reg = droneParts(name=NAME, cPrice=CPR, price=DPR, availability=AVLBTY, featured=FTRD, color=CLR,
#                                 category=CTGRY, label1=label1, input1=input1, label2=label2, currency=CRNCY,
#                                 input2=input2, label3=label3, input3=input3, label4=label4, input4=input4,
#                                 label5=label5, input5=input5, label6=label6, input6=input6,
#                                 description=DESC, image=THMBN)
#             reg.save()
#
#             latest_id = droneParts.objects.latest('id').id
#
#             for f in images:
#                 products = dronePartsImages(images=f, Product_ID_id=latest_id)
#                 products.save()
#
#             PRDTFM = dronePartsForm()
#     else:
#         PRDTFM = dronePartsForm()
#
#     PRDTDT = droneParts.objects.all().order_by('-id')
#     paginator = Paginator(PRDTDT, 10)
#     pageNo = request.GET.get('page')
#     BLGdataFINAL = paginator.get_page(pageNo)
#     totalPages = BLGdataFINAL.paginator.num_pages
#     context = {'form': PRDTFM, 'PRDTDT': BLGdataFINAL, 'lastPage': totalPages, 'pageList': [n + 1 for n in range(totalPages)]}
#     return render(request, 'adminDroneParts.html', context)


@login_required(login_url='/user_login')
@admin_only
def adminHomeSRFP(request):
    if request.method == 'POST':
        SRFPFM = HomeSRFPForm(request.POST, request.FILES)
        if SRFPFM.is_valid():
            SC = SRFPFM.cleaned_data['satisfied_clients']
            RS = SRFPFM.cleaned_data['resolution']
            FT = SRFPFM.cleaned_data['flight_time']
            PD = SRFPFM.cleaned_data['project_done']
            reg = HomeSRFP(satisfied_clients=SC, resolution=RS, flight_time=FT, project_done=PD)
            reg.save()
            SRFPFM = HomeSRFPForm()
    else:
        SRFPFM = HomeSRFPForm()
    SRFPDT = HomeSRFP.objects.all()
    return render(request, 'adminHomeSRFP.html', {'form': SRFPFM, 'SRFPDT': SRFPDT})


@login_required(login_url='/user_login')
@admin_only
def adminVideoGallery(request):
    if request.method == 'POST':
        HVGFM = VideoGalleryForm(request.POST, request.FILES)
        if HVGFM.is_valid():
            VL = HVGFM.cleaned_data['video_link']
            ICN = HVGFM.cleaned_data['icon']
            reg = VideoGallery(video_link=VL, icon=ICN)
            reg.save()
            HVGFM = VideoGalleryForm()
    else:
        HVGFM = VideoGalleryForm()
    HVGDT = VideoGallery.objects.all()
    return render(request, 'adminHomeVideoGallery.html', {'form': HVGFM, 'HVGDT': HVGDT})


@login_required(login_url='/user_login')
@admin_only
def adminPeopleSay(request):
    if request.method == 'POST':
        WPSFM = WhatPeopleSForm(request.POST, request.FILES)
        if WPSFM.is_valid():
            NM = WPSFM.cleaned_data['name']
            DESG = WPSFM.cleaned_data['designation']
            SAY = WPSFM.cleaned_data['say_something']
            ICN = WPSFM.cleaned_data['icon']
            reg = WhatPeopleSay(name=NM, designation=DESG, say_something=SAY, icon=ICN)
            reg.save()
            WPSFM = WhatPeopleSForm()
    else:
        WPSFM = WhatPeopleSForm()
    WPSDT = WhatPeopleSay.objects.all()
    return render(request, 'adminPeopleSay.html', {'form': WPSFM, 'WPSDT': WPSDT})


@login_required(login_url='/user_login')
@admin_only
def adminOurPartner(request):
    if request.method == 'POST':
        OPTFM = OurPartnerForm(request.POST, request.FILES)
        if OPTFM.is_valid():
            CN = OPTFM.cleaned_data['company_name']
            DESC = OPTFM.cleaned_data['description']
            LOGO = OPTFM.cleaned_data['logo']
            reg = OurPartner(company_name=CN, description=DESC, logo=LOGO)
            reg.save()
            OPTFM = OurPartnerForm()
    else:
        OPTFM = OurPartnerForm()
    OPTDT = OurPartner.objects.all()
    return render(request, 'adminOurPartner.html', {'form': OPTFM, 'OPTDT': OPTDT})


@login_required(login_url='/user_login')
@admin_only
def adminaboutTitlePost(request):
    if request.method == 'POST':
        ABFM = AboutTitlePostForm(request.POST, request.FILES)
        if ABFM.is_valid():
            TIT = ABFM.cleaned_data['title']
            DSC = ABFM.cleaned_data['description']
            FT1 = ABFM.cleaned_data['feature1']
            FT2 = ABFM.cleaned_data['feature2']
            FT3 = ABFM.cleaned_data['feature3']
            IMG = ABFM.cleaned_data['image']
            reg = AboutTitlePost(title=TIT, description=DSC, feature1=FT1, feature2=FT2, feature3=FT3, image=IMG)
            reg.save()
            ABFM = AboutTitlePostForm()
    else:
        ABFM = AboutTitlePostForm()
    ABTMD = AboutTitlePost.objects.all()
    return render(request, 'adminaboutTitlePost.html', {'form': ABFM, 'ABTMD': ABTMD})


@login_required(login_url='/user_login')
@admin_only
def adminQualityTrust(request):
    if request.method == 'POST':
        QTFM = QualityTrustForm(request.POST, request.FILES)
        if QTFM.is_valid():
            TIT = QTFM.cleaned_data['title']
            DSC = QTFM.cleaned_data['Description']
            ICN = QTFM.cleaned_data['icon']
            reg = QualityTrust(title=TIT, Description=DSC, icon=ICN)
            reg.save()
            QTFM = QualityTrustForm()
    else:
        QTFM = QualityTrustForm()
    data = QualityTrust.objects.all()
    return render(request, 'adminQualityTrust.html', {'form': QTFM, 'QTdata': data})


@login_required(login_url='/user_login')
@admin_only
def adminOurTeam(request):
    if request.method == 'POST':
        OUTFM = OurTeamForm(request.POST, request.FILES)
        if OUTFM.is_valid():
            NM = OUTFM.cleaned_data['name']
            EML = OUTFM.cleaned_data['email']
            PHN = OUTFM.cleaned_data['phone']
            EXPR = OUTFM.cleaned_data['experience']
            DSG = OUTFM.cleaned_data['designation']
            SM1 = OUTFM.cleaned_data['socialmedia1']
            SM2 = OUTFM.cleaned_data['socialmedia2']
            SM3 = OUTFM.cleaned_data['socialmedia3']
            DESC = OUTFM.cleaned_data['description']
            PRF = OUTFM.cleaned_data['profile']
            reg = OurTeam(name=NM, email=EML, phone=PHN, designation=DSG, experience=EXPR, socialmedia1=SM1,
                          socialmedia2=SM2, socialmedia3=SM3, description=DESC, profile=PRF)
            reg.save()
            OUTFM = OurTeamForm()
    else:
        OUTFM = OurTeamForm()
    data = OurTeam.objects.all()
    return render(request, 'adminOurTeam.html', {'form': OUTFM, 'OUTdata': data})


@login_required(login_url='/user_login')
@admin_only
def adminServicesType(request):
    if request.method == 'POST':
        STFM = ServicesTypeForm(request.POST, request.FILES)
        if STFM.is_valid():
            TIT = STFM.cleaned_data['title']
            QT = STFM.cleaned_data['quote']
            QTB = STFM.cleaned_data['quote_by']
            type = STFM.cleaned_data['type']
            HL1 = STFM.cleaned_data['highlight1']
            HL2 = STFM.cleaned_data['highlight2']
            HL3 = STFM.cleaned_data['highlight3']
            HL4 = STFM.cleaned_data['highlight4']
            HL5 = STFM.cleaned_data['highlight5']
            HL6 = STFM.cleaned_data['highlight6']
            DSC = STFM.cleaned_data['Description']
            ICNS = STFM.cleaned_data['icons']
            reg = ServicesTypes(title=TIT, Description=DSC, quote=QT, quote_by=QTB, type=type, highlight1=HL1,
                                highlight2=HL2,
                                highlight3=HL3, highlight4=HL4, highlight5=HL5, highlight6=HL6, icons=ICNS)
            reg.save()
            STFM = ServicesTypeForm()
    else:
        STFM = ServicesTypeForm()
    STdata = ServicesTypes.objects.all()
    return render(request, 'adminServicesType.html', {'form': STFM, 'STdata': STdata})


@login_required(login_url='/user_login')
@admin_only
def adminPricing(request):
    if request.method == 'POST':
        PRCFM = PricingForm(request.POST, request.FILES)
        if PRCFM.is_valid():
            CTG = PRCFM.cleaned_data['category']
            PRC = PRCFM.cleaned_data['price']
            FT1 = PRCFM.cleaned_data['feature1']
            FT2 = PRCFM.cleaned_data['feature2']
            FT3 = PRCFM.cleaned_data['feature3']
            FT4 = PRCFM.cleaned_data['feature4']
            FT5 = PRCFM.cleaned_data['feature5']
            reg = Pricing(category=CTG, price=PRC, feature1=FT1, feature2=FT2, feature3=FT3, feature4=FT4, feature5=FT5)
            reg.save()
            PRCFM = PricingForm()
    else:
        PRCFM = PricingForm()
    PRCdata = Pricing.objects.all()
    return render(request, 'adminPricing.html', {'form': PRCFM, 'PRCdata': PRCdata})


@login_required(login_url='/user_login')
@admin_only
def adminGallery(request):
    if request.method == 'POST':
        GLRFM = GalleryForm(request.POST, request.FILES)
        if GLRFM.is_valid():
            TIT = GLRFM.cleaned_data['title']
            CTG = GLRFM.cleaned_data['category']
            DSC = GLRFM.cleaned_data['description']
            IMG = GLRFM.cleaned_data['image']
            reg = Gallery(title=TIT, category=CTG, description=DSC, image=IMG)
            reg.save()
            GLRFM = GalleryForm()
    else:
        GLRFM = GalleryForm()
    GLRdata = Gallery.objects.all()
    return render(request, 'adminGallery.html', {'form': GLRFM, 'GLRdata': GLRdata})


@login_required(login_url='/user_login')
@admin_only
def adminsocial_media(request):
    if request.method == 'POST':
        SMFM = SocialMediaForm(request.POST, request.FILES)
        if SMFM.is_valid():
            EM = SMFM.cleaned_data['email']
            SK = SMFM.cleaned_data['skype']
            PH = SMFM.cleaned_data['phone']
            GIT = SMFM.cleaned_data['github']
            LIK = SMFM.cleaned_data['linkedin']
            GP = SMFM.cleaned_data['google_plus']
            YTB = SMFM.cleaned_data['youtube']
            FCBK = SMFM.cleaned_data['facebook']
            TWTR = SMFM.cleaned_data['twitter']
            reg = SocialMedia(email=EM, skype=SK, phone=PH, github=GIT, linkedin=LIK, google_plus=GP, youtube=YTB,
                              facebook=FCBK, twitter=TWTR)
            reg.save()
            SMFM = SocialMediaForm()
    else:
        SMFM = SocialMediaForm()
    SMdata = SocialMedia.objects.all()
    return render(request, 'adminSocialmedia.html', {'form': SMFM, 'SMdata': SMdata})


@login_required(login_url='/user_login')
@admin_only
def adminuser_blog(request):
    if request.method == 'POST':
        TIT = request.POST.get('title')
        HD = request.POST.get('heading')
        TGS = request.POST.get('tags')
        QT = request.POST.get('quote')
        QTBY = request.POST.get('quote_by')
        CRA = request.POST.get('created_at')
        DSC = request.POST.get('editor1')
        ICN = request.FILES['icon']
        reg = userBlog(title=TIT, heading=HD, tags=TGS, quote=QT, quote_by=QTBY, description=DSC, Icon=ICN,
                       created_at=CRA)
        reg.save()

    BLGdata = userBlog.objects.all().order_by('-sNo')
    paginator = Paginator(BLGdata, 10)
    pageNo = request.GET.get('page')
    BLGdataFINAL = paginator.get_page(pageNo)
    totalPages = BLGdataFINAL.paginator.num_pages
    context = {'BLGdata': BLGdataFINAL, 'lastPage': totalPages, 'pageList': [n + 1 for n in range(totalPages)]}
    return render(request, 'adminBlog.html', context)


@admin_only
def viewMSG(request, id):
    messages_detail = contact_us.objects.get(id=id)
    return render(request, 'viewMessages.html', {'messages_detail': messages_detail})


@admin_only
def orders(request):
    product_orders = Place_Order.objects.all()
    context = {'product_orders': product_orders}
    return render(request, 'adminOrders.html', context)


@admin_only
def user_comments(request):
    comment_data = blog_Review.objects.all()
    return render(request, 'adminComments.html', {'comment_data': comment_data})

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

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Update Functions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


@login_required(login_url='/user_login')
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
            UpdateForm.title = request.POST.get('title')
            UpdateForm.heading = request.POST.get('heading')
            UpdateForm.tags = request.POST.get('tags')
            UpdateForm.quote = request.POST.get('quote')
            UpdateForm.quote_by = request.POST.get('quote_by')
            UpdateForm.description = request.POST.get('editor1')
            UpdateForm.save()
            return HttpResponseRedirect('/adminblog')

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
