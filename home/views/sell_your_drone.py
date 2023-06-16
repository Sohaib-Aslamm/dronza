from django.shortcuts import render
from home.models import sellYourDrone
from django.core.paginator import Paginator
from dronzaPanel.models import Products, SocialMedia, userBlog, seoTags


def sellDrones(request):
    sellerProducts = sellYourDrone.objects.filter(status='Available').order_by('-id')
    paginator = Paginator(sellerProducts, 8)
    pageNo = request.GET.get('page')
    sellerProductsFINAL = paginator.get_page(pageNo)
    totalPages = sellerProductsFINAL.paginator.num_pages
    Product_Category = sellYourDrone.objects.values('category').distinct()
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    SEOTAGS = seoTags.objects.filter(page='sell_your_drone_page')
    FEATURED = Products.objects.filter(featured='Featured')
    context = {'sellerProducts': sellerProductsFINAL, 'Product_Category': Product_Category, 'lastPage': totalPages,
               'pageList': [n + 1 for n in range(totalPages)], 'RCPST': RCPST, 'SMDT': SMDT, 'FEATURED': FEATURED,
               'SEOTAGS': SEOTAGS}
    return render(request, 'sellDrone.html', context)


def search_by_location(request):
    location = request.GET.get('location') or request.POST.get('location')
    sellerProducts = sellYourDrone.objects.all()  # Initialize as an empty queryset

    if location:
        sellerProducts = sellYourDrone.objects.filter(location__icontains=location).order_by('-id')

    paginator = Paginator(sellerProducts, 8)
    pageNo = request.GET.get('page')
    sellerProductsFINAL = paginator.get_page(pageNo)
    totalPages = sellerProductsFINAL.paginator.num_pages

    Product_Category = sellerProducts.values('category').distinct()
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    SEOTAGS = seoTags.objects.filter(page='sell_your_drone_search_by_location')
    FEATURED = Products.objects.filter(featured='Featured')

    context = {
        'sellerProducts': sellerProductsFINAL,
        'Product_Category': Product_Category,
        'lastPage': totalPages,
        'pageList': [n + 1 for n in range(totalPages)],
        'RCPST': RCPST,
        'SMDT': SMDT,
        'FEATURED': FEATURED,
        'SEOTAGS': SEOTAGS,
        'location': location,  # Include location in the context
    }

    return render(request, 'search_seller_product.html', context)
