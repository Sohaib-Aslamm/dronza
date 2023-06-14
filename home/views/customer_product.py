from django.shortcuts import render
from django.core.paginator import Paginator
from dronzaPanel.models import SocialMedia, userBlog, seoTags
from home.models import sellYourDrone, sellYourDroneImages


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
    SYDProducts = sellYourDrone.objects.filter(user_id=user_id)
    paginator = Paginator(SYDProducts, 8)
    pageNo = request.GET.get('page')
    SYDProductsFINAL = paginator.get_page(pageNo)
    totalPages = SYDProductsFINAL.paginator.num_pages
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    SEOTAGS = seoTags.objects.filter(page='customer_product_panel_page')

    context = {
        'SYDProducts': SYDProductsFINAL,
        'lastPage': totalPages,
        'pageList': [n + 1 for n in range(totalPages)],
        'RCPST': RCPST,
        'SMDT': SMDT,
        'SEOTAGS': SEOTAGS
    }
    return render(request, 'customerProducts.html', context)
