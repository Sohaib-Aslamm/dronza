from dronzaPanel.forms import ServicesTypeForm, PricingForm, GalleryForm
from dronzaPanel.models import ServicesTypes, Pricing, Gallery

from django.shortcuts import render

from dronzaPanel.decorators import admin_only, custom_login_required


# Create your views here


@custom_login_required
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


@custom_login_required
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


@custom_login_required
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