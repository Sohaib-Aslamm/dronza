from django.shortcuts import render
from django.db.models import Q

from home.enumerators import SOLD_STATUS
from home.models import sellYourDrone
from django.core.paginator import Paginator
from dronzaPanel.models import SocialMedia, userBlog, seoTags, MainSlider
from django.urls import reverse


def sellDrones(request, page_number=None):
    seller_products = sellYourDrone.objects.filter(status=SOLD_STATUS.AVAILABLE).order_by('-id')
    paginator = Paginator(seller_products, 8)
    seller_products_final = paginator.get_page(page_number)
    total_pages = seller_products_final.paginator.num_pages
    product_category = sellYourDrone.objects.values('category').distinct()
    recent_blog_post = userBlog.objects.order_by('-sNo')[:2]
    social_media = SocialMedia.objects.all()
    slider = MainSlider.objects.filter(page='sell_drones_page')

    canonical_link = reverse('sell-drones')  # Assuming 'blog' is the name of your URL pattern
    if page_number:
        canonical_link += f'/page/{page_number}'
    seo_tags = [{
        'title': "Sell Your Drone or Accessories on DronZa - List for Free!",
        'description': "List your drone for sale free of cost on our platform. Take advantage of this unique feature "
                       "provided by DronZa to sell your drone hassle-free.",
        'tags': "Sell Your Drone Drone For Sale Drone Accessories Sell My Drone Drone Marketplace drone accessories for"
                " sale drone-parts-for-sale drone-listing-platform drone-classifieds drone-marketplace",
        'canonical_link': request.build_absolute_uri(canonical_link)
    }]

    featured_listings = sellYourDrone.objects.filter(is_featured=True, status=SOLD_STATUS.AVAILABLE)
    context = {'sellerProducts': seller_products_final, 'Product_Category': product_category, 'lastPage': total_pages,
               'pageList': [n + 1 for n in range(total_pages)], 'RCPST': recent_blog_post, 'SMDT': social_media,
               'FEATURED': featured_listings, 'SEOTAGS': seo_tags, 'SLIDER': slider}
    return render(request, 'sellDrone.html', context)


def search_by_location(request):
    location = request.GET.get('location') or request.POST.get('location')
    sellerProducts = sellYourDrone.objects.all()  # Initialize as an empty queryset

    if location:
        sellerProducts = sellYourDrone.objects.filter(
            Q(location__icontains=location) &
            Q(status='Available')
        ).order_by('-id')

    paginator = Paginator(sellerProducts, 8)
    pageNo = request.GET.get('page')
    sellerProductsFINAL = paginator.get_page(pageNo)
    totalPages = sellerProductsFINAL.paginator.num_pages

    Product_Category = sellerProducts.values('category').distinct()
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    SEOTAGS = seoTags.objects.filter(page='sell_your_drone_search_by_location')
    FEATURED = sellYourDrone.objects.filter(is_featured=True)
    SLIDER = MainSlider.objects.filter(page='sell_drones_search_page')

    context = {
        'sellerProducts': sellerProductsFINAL,
        'Product_Category': Product_Category,
        'lastPage': totalPages,
        'pageList': [n + 1 for n in range(totalPages)],
        'RCPST': RCPST,
        'SMDT': SMDT,
        'FEATURED': FEATURED,
        'SEOTAGS': SEOTAGS,
        'location': location,
        'SLIDER': SLIDER,
    }

    return render(request, 'search_seller_product.html', context)
