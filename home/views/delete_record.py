from django.shortcuts import render, redirect

from home.commands import Data_Logger
from home.enumerators import DJANGO_VIEWS
from home.models import sellYourDrone


def delete_record_by_uuid(request, record_type, slug):
    try:
        if record_type == 'customer-product':
            sellYourDrone.objects.filter(slug=slug).delete()
            return redirect('/customer-product')
    except Exception as e:
        Data_Logger.log_error_message(DJANGO_VIEWS.DELETE_RECORD, e, Data_Logger.get_client_ip(request))
        return redirect('error-404')
