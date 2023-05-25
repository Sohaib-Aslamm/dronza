from django.shortcuts import render
from home.models import sellYourDrone
from django.core.paginator import Paginator
from dronzaPanel.models import Products, SocialMedia, userBlog


def sellDrones(request):
    sellerProducts = sellYourDrone.objects.filter(status='Available')
    paginator = Paginator(sellerProducts, 8)
    pageNo = request.GET.get('page')
    sellerProductsFINAL = paginator.get_page(pageNo)
    totalPages = sellerProductsFINAL.paginator.num_pages
    Product_Category = sellYourDrone.objects.values('category').distinct()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    FEATURED = Products.objects.filter(featured='Featured')
    context = {'sellerProducts': sellerProductsFINAL, 'Product_Category': Product_Category, 'lastPage': totalPages,
               'pageList': [n + 1 for n in range(totalPages)], 'RCPST': RCPST, 'SMDT': SMDT, 'FEATURED': FEATURED}
    return render(request, 'sellDrone.html', context)