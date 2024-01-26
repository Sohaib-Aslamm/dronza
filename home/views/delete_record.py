from django.shortcuts import render, redirect
from home.models import sellYourDrone


def delete_record_by_uuid(request, record_type, slug):
    if record_type == 'customer-product':
        sellYourDrone.objects.filter(slug=slug).delete()
        return redirect('/customer-product')
