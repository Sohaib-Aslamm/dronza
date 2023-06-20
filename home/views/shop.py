from django.shortcuts import render
from django.core.paginator import Paginator
from dronzaPanel.models import Products, SocialMedia, userBlog, MainSlider
from django.urls import reverse


def shop(request, page_number=None):
    dronzaProducts = Products.objects.all().order_by('-id')
    dronzapaginator = Paginator(dronzaProducts, 50)
    dronzaProductsFINAL = dronzapaginator.get_page(page_number)
    dronzatotalPages = dronzaProductsFINAL.paginator.num_pages
    DRONZATGRY = Products.objects.values('category').distinct()
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    FEATURED = Products.objects.filter(featured='Featured')
    SLIDER = MainSlider.objects.filter(page='shop_page')

    canonical_link = reverse('shop')  # Assuming 'blog' is the name of your URL pattern

    if page_number:
        canonical_link += f'/page/{page_number}'

    SEOTAGS = [{
        'title': "Dronza - Shop Drones and Drone Accessories",
        'description': "Welcome to our shop, where you can explore a wide range of drone products. Shop now and elevate your drone experience with Dronza.org",
        'tags': "Drone Shop Drone Products Drone Accessories Metal Products Fabric Products Wireless Products Plastic Products Titanium Products Aluminum Products Drone Parts Online Shopping Dronza Org drones drone parts drone shipping drone returns drone warranty",
        'canonical_link': request.build_absolute_uri(canonical_link)
    }]

    context = {'dronzaProductsFINAL': dronzaProductsFINAL,
               'dronzalastPage': dronzatotalPages, 'dronzatotalPages': dronzatotalPages,
               'dronzapageList': [n + 1 for n in range(dronzatotalPages)], 'DRONZATGRY': DRONZATGRY,
               'FEATURED': FEATURED, 'RCPST': RCPST, 'SMDT': SMDT, 'SEOTAGS': SEOTAGS, 'SLIDER': SLIDER}
    return render(request, 'dronzaShop.html', context)


