from django.shortcuts import render, redirect
from home.models import sellYourDrone


def DeletebyUUID(request, type, slug):
    if type == 'customerProduct':
        sellYourDrone.objects.filter(slug=slug).delete()
        return redirect('/customerProduct')
