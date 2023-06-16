from dronzaPanel.models import Products, productImages, VideoGallery
from dronzaPanel.forms import VideoGalleryForm

from django.shortcuts import render

from dronzaPanel.decorators import admin_only, custom_login_required
from django.core.paginator import Paginator


@custom_login_required
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


@custom_login_required
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