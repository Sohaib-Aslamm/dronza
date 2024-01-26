from django.shortcuts import render, redirect

from dronzaPanel.models import MainSlider
from home.enumerators import PRODUCT_CATEGORY, SOLD_STATUS, DRONE_COLOR, DRONE_CONDITION, DRONE_BRAND, SPEED_MODE, \
    WING_TYPE, PRODUCT_TYPE
from home.models import sellYourDrone


def UpdatebyUUID(request, type, slug):
    if type == 'customer-product':

        Record = sellYourDrone.objects.get(slug=slug)
        if request.method == 'POST':
            Record.name = request.POST.get('name')
            Record.email = request.POST.get('email')
            Record.pPhone = request.POST.get('pPhone')
            Record.sPhone = request.POST.get('sPhone')
            Record.address = request.POST.get('address')
            Record.title = request.POST.get('title')
            Record.product_category = request.POST.get('product_category')
            Record.product_type = request.POST.get('product_type')
            Record.condition = request.POST.get('condition')
            Record.price = request.POST.get('price')
            Record.color = request.POST.get('color')
            Record.brand = request.POST.get('brand')
            Record.speed_mode = request.POST.get('speed_mode')
            Record.wing_type = request.POST.get('wing_type')
            Record.drone_model = request.POST.get('drone_model')
            Record.noise_level = request.POST.get('noise_level')
            Record.status = request.POST.get('status')
            Record.description = request.POST.get('editor1')

            file_data = request.POST.get('edit_file')
            if not file_data == 'False':
                Record.thumbnail = request.FILES['thumbnail']

            Record.save()
            return redirect('/customer-product')
        main_slider = MainSlider.objects.filter(page='edit_customer_product_page')
        context = {
            'product_category': PRODUCT_CATEGORY.choices,
            'product_type': PRODUCT_TYPE.choices,
            'speed_mode': SPEED_MODE.choices,
            'wing_type': WING_TYPE.choices,
            'brand': DRONE_BRAND.choices,
            'condition': DRONE_CONDITION.choices,
            'color': DRONE_COLOR.choices,
            'status': SOLD_STATUS.choices,
            'main_slider': main_slider,
            'Record': Record,
        }
        return render(request, 'update/customerProducts.html', context)
