from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from dronzaPanel.models import SocialMedia, userBlog
from home.models import sellYourDrone, sellYourDroneImages
from django.urls import reverse


def customerProduct(request):
    if request.method == 'POST':

        form_data = {
            'user_id': request.POST.get('user_id'),
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'pPhone': request.POST.get('pPhone'),
            'sPhone': request.POST.get('sPhone'),
            'location': request.POST.get('location'),
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
        sv = sellYourDrone.objects.create(**form_data)
        latest_id = sv.id

        images = request.FILES.getlist('images')
        for f in images:
            sellYourDroneImages.objects.create(images=f, Product_ID_id=latest_id)

    user_id = request.user.id
    SYDProducts = sellYourDrone.objects.filter(
                                                Q(user_id=user_id) &
                                                Q(status='Available') |
                                                Q(status='Featured')
                                            ).order_by('-id')

    paginator = Paginator(SYDProducts, 8)
    pageNo = request.GET.get('page')
    SYDProductsFINAL = paginator.get_page(pageNo)
    totalPages = SYDProductsFINAL.paginator.num_pages
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()

    current_page = request.GET.get('page')
    canonical_link = reverse('customer-product')  # Assuming 'blog' is the name of your URL pattern

    if current_page:
        canonical_link += f'?page={current_page}'

    SEOTAGS = [{
        'title': "Customer Product Management Panel | Dronza",
        'description': "Manage your listed drone products with ease through the Customer Product Management Panel at Dronza. Update, add, or delete products.",
        'tags': "Product Management Sell Your Drone Drone Listing Customer Panel Complaint Center customer-product-management-panel drone-product-management-panel drone-listing-platform drone-classifieds drone-marketplace drone-complaints",
        'canonical_link': request.build_absolute_uri(canonical_link)
    }]

    context = {
        'SYDProducts': SYDProductsFINAL,
        'lastPage': totalPages,
        'pageList': [n + 1 for n in range(totalPages)],
        'RCPST': RCPST,
        'SMDT': SMDT,
        'SEOTAGS': SEOTAGS
    }
    return render(request, 'customerProducts.html', context)
