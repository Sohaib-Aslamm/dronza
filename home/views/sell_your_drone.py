from django.shortcuts import render
from django.db.models import Q

from home.enumerators import SOLD_STATUS, DRONE_CATEGORY, DRONE_BRAND, DRONE_CONDITION
from home.models import sellYourDrone
from django.core.paginator import Paginator
from dronzaPanel.models import SocialMedia, userBlog, seoTags, MainSlider
from django.urls import reverse


def sellDrones(request, page_number=None):
    seller_products = sellYourDrone.objects.filter(status=SOLD_STATUS.AVAILABLE).order_by('-id')
    paginator = Paginator(seller_products, 8)
    seller_products_final = paginator.get_page(page_number)
    total_pages = seller_products_final.paginator.num_pages
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
    context = {
        'sellerProducts': seller_products_final,
        'categories': DRONE_CATEGORY.choices,
        'brand': DRONE_BRAND.choices,
        'condition': DRONE_CONDITION.choices,
        'lastPage': total_pages,
        'pageList': [n + 1 for n in range(total_pages)],
        'RCPST': recent_blog_post,
        'SMDT': social_media,
        'FEATURED': featured_listings,
        'SEOTAGS': seo_tags,
        'SLIDER': slider
    }
    return render(request, 'sellDrone.html', context)


def search_by_location_category(request):
    # Get filter parameters from the request
    location = request.GET.get('location') or request.POST.get('location')
    category = request.GET.get('category') or request.POST.get('category')
    brand = request.GET.get('brand') or request.POST.get('brand')
    condition = request.GET.get('condition') or request.POST.get('condition')

    # Initialize filter conditions
    filter_conditions = Q(status='Available')

    # Add location filter
    if location:
        filter_conditions &= Q(location__icontains=location)

    # Add category filter
    if category and category != 'select category':
        filter_conditions &= Q(category=category)

    # Add brand filter
    if brand and brand != 'select brand':
        filter_conditions &= Q(brand=brand)

    # Add condition filter
    if condition and condition != 'select condition':
        filter_conditions &= Q(condition=condition)

    listing_products = sellYourDrone.objects.all()

    # Apply filters to the queryset
    listing_products = sellYourDrone.objects.filter(filter_conditions).order_by('-id')

    # Pagination
    paginator = Paginator(listing_products, 8)
    page_no = request.GET.get('page')
    seller_products_final = paginator.get_page(page_no)
    total_pages = seller_products_final.paginator.num_pages

    # Additional data
    rcpst = userBlog.objects.order_by('-sNo')[:2]
    sdmt = SocialMedia.objects.all()
    seo_tags = seoTags.objects.filter(page='sell_your_drone_search_by_location')
    featured = sellYourDrone.objects.filter(is_featured=True)
    slider = MainSlider.objects.filter(page='sell_drones_search_page')

    context = {
        'sellerProducts': seller_products_final,
        'lastPage': total_pages,
        'pageList': range(1, total_pages + 1),
        'categories_list': DRONE_CATEGORY.choices,
        'brands_list': DRONE_BRAND.choices,
        'conditions_list': DRONE_CONDITION.choices,
        'RCPST': rcpst,
        'SMDT': sdmt,
        'FEATURED': featured,
        'SEOTAGS': seo_tags,
        'location': location,
        'category': category,
        'brand': brand,
        'condition': condition,
        'SLIDER': slider,
    }

    return render(request, 'search_seller_product.html', context)
