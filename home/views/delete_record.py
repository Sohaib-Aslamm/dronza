from django.shortcuts import render, redirect
from home.models import sellYourDrone


def DeletebyUUID(request, uuid, type):
    if type == 'sellerProduct':
        sellYourDrone.objects.filter(uuid=uuid).delete()
        return redirect('/customerProduct')