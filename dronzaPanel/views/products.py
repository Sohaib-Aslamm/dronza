from dronzaPanel.models import Products, productImages, VideoGallery
from dronzaPanel.forms import VideoGalleryForm

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dronzaPanel.decorators import admin_only
from django.core.paginator import Paginator


@login_required(login_url='/user-login')
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
        TGS = request.POST.get('tags')
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
                       category=CTR, featured=FTRD, description=description, label1=lbl1, label2=lbl2, tags=TGS,
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
# @login_required(login_url='/user-login')
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


@login_required(login_url='/user-login')
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