from django.shortcuts import render, redirect
from home.models import sellYourDrone


def DeletebyUUID(request, uuid, type):
    if type == 'sellerProduct':
        DeleteRecord = sellYourDrone.objects.get(uuid=uuid)
        DeleteRecord.delete()
        return redirect('/customerProduct')