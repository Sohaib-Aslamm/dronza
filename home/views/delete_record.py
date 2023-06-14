from django.shortcuts import render, redirect
from home.models import sellYourDrone


def DeletebyUUID(request, type, slug):
    if type == 'customer-product':
        sellYourDrone.objects.filter(slug=slug).delete()
        return redirect('/customer-product')
