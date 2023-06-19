from dronzaPanel.forms import MainSliderForm, HomeHIWForm, HomeHTUForm, HomeAboutForm, AboutTitlePostForm, \
    QualityTrustForm
from dronzaPanel.models import MainSlider, HomeHIW, HomeHTU, HomeAbout, AboutTitlePost, QualityTrust

from home.models import contact_us, Place_Order, blog_Review

from django.shortcuts import render

from dronzaPanel.decorators import admin_only, custom_login_required

# Create your views here


@custom_login_required
@admin_only
def adminHome(request):
    my_messages = contact_us.objects.all()
    return render(request, 'HomeAdmin.html', {'my_messages': my_messages})


@custom_login_required
@admin_only
def adminHomeSlider(request):
    if request.method == 'POST':
        MSFM = MainSliderForm(request.POST, request.FILES)
        if MSFM.is_valid():
            TIT = MSFM.cleaned_data['title']
            PAGE = MSFM.cleaned_data['page']
            IMG = MSFM.cleaned_data['image']
            BKIMG = MSFM.cleaned_data['background_image']
            reg = MainSlider(title=TIT, page=PAGE, image=IMG, background_image=BKIMG)
            reg.save()
            MSFM = MainSliderForm()
    else:
        MSFM = MainSliderForm()
    SLDT = MainSlider.objects.all()
    return render(request, 'adminHomeSlider.html', {'SLDT': SLDT, 'form': MSFM})


@custom_login_required
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


@custom_login_required
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


@custom_login_required
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


@custom_login_required
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


@custom_login_required
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


@custom_login_required
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
