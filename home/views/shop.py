from django.shortcuts import render
from django.core.paginator import Paginator
from dronzaPanel.models import Products, SocialMedia, userBlog
from django.urls import reverse


def shop(request):
    dronzaProducts = Products.objects.all().order_by('-id')
    dronzapaginator = Paginator(dronzaProducts, 50)
    dronzapageNo = request.GET.get('page')
    dronzaProductsFINAL = dronzapaginator.get_page(dronzapageNo)
    dronzatotalPages = dronzaProductsFINAL.paginator.num_pages
    DRONZATGRY = Products.objects.values('category').distinct()
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    FEATURED = Products.objects.filter(featured='Featured')

    current_page = request.GET.get('page')
    canonical_link = reverse('shop')  # Assuming 'blog' is the name of your URL pattern

    if current_page:
        canonical_link += f'?page={current_page}'

    SEOTAGS = [{
        'title': "Dronza - Shop Drones and Drone Accessories",
        'description': "Welcome to our shop, where you can explore a wide range of drone products. Shop now and elevate your drone experience with Dronza.org",
        'tags': "Drone Shop Drone Products Drone Accessories Metal Products Fabric Products Wireless Products Plastic Products Titanium Products Aluminum Products Drone Parts Online Shopping Dronza Org drones drone parts drone shipping drone returns drone warranty",
        'canonical_link': request.build_absolute_uri(canonical_link)
    }]

    context = {'dronzaProductsFINAL': dronzaProductsFINAL,
               'dronzalastPage': dronzatotalPages, 'dronzatotalPages': dronzatotalPages,
               'dronzapageList': [n + 1 for n in range(dronzatotalPages)], 'DRONZATGRY': DRONZATGRY,
               'FEATURED': FEATURED, 'RCPST': RCPST, 'SMDT': SMDT, 'SEOTAGS': SEOTAGS}
    return render(request, 'dronzaShop.html', context)


