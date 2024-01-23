from django.shortcuts import render, redirect
from django.contrib import messages
from geopy.geocoders import Nominatim
from django.core.paginator import Paginator
from dronzaPanel.models import SocialMedia, userBlog, MainSlider
from home.enumerators import DRONE_CATEGORY, DRONE_BRAND, DRONE_CONDITION, DRONE_COLOR, SOLD_STATUS
from home.models import sellYourDrone, sellYourDroneImages
from django.urls import reverse


def customer_product(request, page_number=None):
    if request.method == 'POST':
        geolocator = Nominatim(user_agent="my_app")  # Replace "my_app" with your application name

        location = geolocator.reverse((request.POST.get('latitude'), request.POST.get('longitude')), language='en')

        # Extract relevant information from the location object
        user_location = location.address if location else "Location not found"

        form_data = {
            'user': request.user,
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'pPhone': request.POST.get('pPhone'),
            'sPhone': request.POST.get('sPhone'),
            'location': user_location,
            'address': request.POST.get('address'),
            'title': request.POST.get('title'),
            'price': request.POST.get('price'),
            'category': request.POST.get('category'),
            'brand': request.POST.get('brand'),
            'color': request.POST.get('color'),
            'condition': request.POST.get('condition'),
            'status': request.POST.get('status'),
            'label1': request.POST.get('label1'),
            'input1': request.POST.get('input1'),
            'label2': request.POST.get('label2'),
            'input2': request.POST.get('input2'),
            'label3': request.POST.get('label3'),
            'input3': request.POST.get('input3'),
            'label4': request.POST.get('label4'),
            'input4': request.POST.get('input4'),
            'description': request.POST.get('description'),
            'thumbnail': request.FILES['thumbnail'],
        }
        selling_resource = sellYourDrone.objects.create(**form_data)

        images = request.FILES.getlist('images')
        for image in images:
            sellYourDroneImages.objects.create(image=image, Product=selling_resource)
    if request.user.is_anonymous:
        messages.error(request, 'please login in order to list your product')
        return redirect('user-login')
    paginator = Paginator(sellYourDrone.objects.filter(user=request.user).order_by('-id'), 8)
    customer_products = paginator.get_page(page_number)

    canonical_link = reverse('customer-product')  # Assuming 'blog' is the name of your URL pattern

    if page_number:
        canonical_link += f'/page/{page_number}'

    seo_tags = [{
        'title': "Customer Product Management Panel | Dronza",
        'description': "Manage your listed drone products with ease through the Customer Product Management Panel at "
                       "Dronza. Update, add, or delete products.",
        'tags': "Product Management Sell Your Drone Drone Listing Customer Panel Complaint Center customer product "
                "management-panel drone-product-management-panel drone-listing-platform drone-classifieds "
                "drone-marketplace drone-complaints",
        'canonical_link': request.build_absolute_uri(canonical_link)
    }]

    context = {
        'customer_products': customer_products,
        'lastPage': customer_products.paginator.num_pages,
        'page_list': [n + 1 for n in range(customer_products.paginator.num_pages)],
        'RCPST': userBlog.objects.order_by('-sNo')[:2],
        'social_media': SocialMedia.objects.all(),
        'seo_tags': seo_tags,
        'main_slider': MainSlider.objects.filter(page='customer_product_page'),
        'categories': DRONE_CATEGORY.choices,
        'brand': DRONE_BRAND.choices,
        'condition': DRONE_CONDITION.choices,
        'color': DRONE_COLOR.choices,
    }
    return render(request, 'customerProducts.html', context)
