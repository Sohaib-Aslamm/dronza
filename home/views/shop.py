from django.shortcuts import render
from django.core.paginator import Paginator
from dronzaPanel.models import Products, SocialMedia, userBlog, productImages, seoTags
from home.models import productReview


def shop(request):
    dronzaProducts = Products.objects.all().order_by('-id')
    dronzapaginator = Paginator(dronzaProducts, 50)
    dronzapageNo = request.GET.get('page')
    dronzaProductsFINAL = dronzapaginator.get_page(dronzapageNo)
    dronzatotalPages = dronzaProductsFINAL.paginator.num_pages
    DRONZATGRY = Products.objects.values('category').distinct()
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    SEOTAGS = seoTags.objects.filter(page='shop_page')
    FEATURED = Products.objects.filter(featured='Featured')

    context = {'dronzaProductsFINAL': dronzaProductsFINAL,
               'dronzalastPage': dronzatotalPages, 'dronzatotalPages': dronzatotalPages,
               'dronzapageList': [n + 1 for n in range(dronzatotalPages)], 'DRONZATGRY': DRONZATGRY,
               'FEATURED': FEATURED, 'RCPST': RCPST, 'SMDT': SMDT, 'SEOTAGS': SEOTAGS}
    return render(request, 'dronzaShop.html', context)


def shopDetail(request, id, uuid,  type):
    if type == 'dronzaProduct':
        shpDetail = Products.objects.get(id=id, uuid=uuid)
        prd_images = productImages.objects.filter(Product_ID_id=id)
        PRDRVW = Products.objects.filter(id=id)
        coments = productReview.objects.filter(product__in=PRDRVW)
        RCPST = userBlog.objects.order_by('-sNo')[:2]
        SMDT = SocialMedia.objects.all()

        context = {'shpDetail': shpDetail, 'prd_images': prd_images, 'RCPST': RCPST, 'SMDT': SMDT, 'coments': coments}
        return render(request, 'dronzashopDetails.html', context)