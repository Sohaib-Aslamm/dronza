from django.shortcuts import render
from django.db.models import Q

from home.enumerators import SOLD_STATUS, PRODUCT_TYPE, DRONE_BRAND, DRONE_CONDITION, PRODUCT_CATEGORY, SPEED_MODE, \
    WING_TYPE
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
        'product_type': PRODUCT_TYPE.choices,
        'product_category': PRODUCT_CATEGORY.choices,
        'speed_mode': SPEED_MODE.choices,
        'wing_type': WING_TYPE.choices,
        'brand': DRONE_BRAND.choices,
        'condition': DRONE_CONDITION.choices,
        'lastPage': total_pages,
        'pageList': [n + 1 for n in range(total_pages)],
        'recent_blog_post': userBlog.objects.order_by('-sNo')[:2],
        'social_media': SocialMedia.objects.all(),
        'seo_tags': seo_tags,
        'FEATURED': featured_listings,
        'SLIDER': slider
    }
    return render(request, 'sellDrone.html', context)


def search_by_location_category(request):
    # Get filter parameters from the request whether it is GET or POST request
    product_type = request.GET.get('product_type') or request.POST.get('product_type')
    product_category = request.GET.get('product_category') or request.POST.get('product_category')
    brand = request.GET.get('brand') or request.POST.get('brand')
    condition = request.GET.get('condition') or request.POST.get('condition')
    speed_mode = request.GET.get('speed_mode') or request.POST.get('speed_mode')
    wing_type = request.GET.get('wing_type') or request.POST.get('wing_type')
    location = request.GET.get('location') or request.POST.get('location')

    # Initialize filter conditions
    filter_conditions = Q(status='Available')

    # Add location filter
    if location:
        filter_conditions &= Q(location__icontains=location)

    # Add product type filter
    if product_type and product_type != 'select type':
        filter_conditions &= Q(product_type=product_type)

    # Add product category filter
    if product_category and product_category != 'select category':
        filter_conditions &= Q(product_category=product_category)

    # Add brand filter
    if brand and brand != 'select brand':
        filter_conditions &= Q(brand=brand)

    # Add condition filter
    if condition and condition != 'select condition':
        filter_conditions &= Q(condition=condition)

    # Add speed mode filter
    if speed_mode and speed_mode != 'speed mode':
        filter_conditions &= Q(speed_mode=speed_mode)

    # Add wing type filter
    if wing_type and wing_type != 'speed mode':
        filter_conditions &= Q(wing_type=wing_type)

    listing_products = sellYourDrone.objects.all()

    # Apply filters to the queryset
    listing_products = sellYourDrone.objects.filter(filter_conditions).order_by('-id')

    # Pagination
    paginator = Paginator(listing_products, 8)
    page_no = request.GET.get('page')
    seller_products_final = paginator.get_page(page_no)
    total_pages = seller_products_final.paginator.num_pages

    context = {
        'sellerProducts': seller_products_final,
        'lastPage': total_pages,
        'pageList': range(1, total_pages + 1),
        'recent_blog_post': userBlog.objects.order_by('-sNo')[:2],
        'social_media': SocialMedia.objects.all(),
        'seo_tags': seoTags.objects.filter(page='sell_your_drone_search_by_location'),
        'FEATURED': sellYourDrone.objects.filter(is_featured=True),

        # choices to loop from enumerators to select or change
        'product_choices': PRODUCT_TYPE.choices,
        'category_choices': PRODUCT_CATEGORY.choices,
        'brands_choices': DRONE_BRAND.choices,
        'condition_choices': DRONE_CONDITION.choices,
        'speed_mode_choices': SPEED_MODE.choices,
        'wing_type_choices': WING_TYPE.choices,

        # to choose or show selected choice in filters to retain filters selected
        'product_type': product_type,
        'product_category': product_category,
        'brand': brand,
        'condition': condition,
        'speed_mode': speed_mode,
        'wing_type': wing_type,
        'location': location,

        'SLIDER': MainSlider.objects.filter(page='sell_drones_search_page'),
    }

    return render(request, 'search_seller_product.html', context)
