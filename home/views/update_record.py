from django.shortcuts import render, redirect

from dronzaPanel.models import MainSlider, userBlog, SocialMedia
from home.commands import Data_Logger
from home.enumerators import PRODUCT_CATEGORY, SOLD_STATUS, DRONE_COLOR, DRONE_CONDITION, DRONE_BRAND, SPEED_MODE, \
    WING_TYPE, PRODUCT_TYPE, DJANGO_VIEWS
from home.models import sellYourDrone


def update_record_by_uuid(request, record_type, slug):
    try:
        if record_type == 'customer-product':

            instance = sellYourDrone.objects.get(slug=slug)
            if request.method == 'POST':
                instance.name = request.POST.get('name')
                instance.email = request.POST.get('email')
                instance.pPhone = request.POST.get('pPhone')
                instance.sPhone = request.POST.get('sPhone')
                instance.address = request.POST.get('address')
                instance.title = request.POST.get('title')
                instance.product_category = request.POST.get('product_category')
                instance.product_type = request.POST.get('product_type')
                instance.condition = request.POST.get('condition')
                instance.price = request.POST.get('price')
                instance.color = request.POST.get('color')
                instance.brand = request.POST.get('brand')
                instance.speed_mode = request.POST.get('speed_mode')
                instance.wing_type = request.POST.get('wing_type')
                instance.drone_model = request.POST.get('drone_model')
                instance.noise_level = request.POST.get('noise_level')
                instance.status = request.POST.get('status')
                instance.description = request.POST.get('editor1')

                file_data = request.POST.get('edit_file')
                if not file_data == 'False':
                    instance.thumbnail = request.FILES['thumbnail']

                instance.save()
                return redirect('/customer-product')
            seo_tags = [{'title': instance.title, 'description': instance.description[:160], 'tags': instance.title,
                         'canonical_link': f'https://dronza.org/customer-product/{instance.slug}/update'}]
            context = {
                'product_category': PRODUCT_CATEGORY.choices,
                'product_type': PRODUCT_TYPE.choices,
                'speed_mode': SPEED_MODE.choices,
                'wing_type': WING_TYPE.choices,
                'brand': DRONE_BRAND.choices,
                'condition': DRONE_CONDITION.choices,
                'color': DRONE_COLOR.choices,
                'status': SOLD_STATUS.choices,
                'main_slider': MainSlider.objects.filter(page='edit_customer_product_page'),
                'recent_blog_post': userBlog.objects.order_by('-sNo')[:2],
                'social_media': SocialMedia.objects.all(),
                'seo_tags': seo_tags,
                'Record': instance,
            }
            return render(request, 'update/customerProducts.html', context)
    except Exception as e:
        Data_Logger.log_error_message(DJANGO_VIEWS.UPDATE_RECORD, e, Data_Logger.get_client_ip(request))
        return redirect('error-404')
