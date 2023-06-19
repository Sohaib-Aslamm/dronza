from django.shortcuts import render, redirect
from home.models import sellYourDrone


def UpdatebyUUID(request, type, slug):
    if type == 'customer-product':

        Record = sellYourDrone.objects.get(slug=slug)
        if request.method == 'POST':
            Record.name = request.POST.get('name')
            Record.email = request.POST.get('email')
            Record.pPhone = request.POST.get('pPhone')
            Record.sPhone = request.POST.get('sPhone')
            Record.location = request.POST.get('location')
            Record.title = request.POST.get('title')
            Record.category = request.POST.get('category')
            Record.condition = request.POST.get('condition')
            Record.price = request.POST.get('price')
            Record.color = request.POST.get('color')
            Record.brand = request.POST.get('brand')
            Record.status = request.POST.get('status')
            Record.label1 = request.POST.get('label1')
            Record.input1 = request.POST.get('input1')
            Record.label2 = request.POST.get('label2')
            Record.input2 = request.POST.get('input2')
            Record.label3 = request.POST.get('label3')
            Record.input3 = request.POST.get('input3')
            Record.label4 = request.POST.get('label4')
            Record.input4 = request.POST.get('input4')
            Record.description = request.POST.get('description')

            file_data = request.POST.get('edit_file')
            if not file_data == 'False':
                Record.thumbnail = request.FILES['thumbnail']

            Record.save()
            return redirect('/customer-product')
        return render(request, 'update/customerProducts.html', {'Record': Record})
