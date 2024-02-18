from django.shortcuts import render, redirect

from home.commands import Data_Logger
from home.enumerators import DJANGO_VIEWS
from home.models import NewsLetterSubscriber


def news_letter_subscriber(request):
    try:
        if request.method == 'POST':
            save_subscriber = NewsLetterSubscriber(email=request.POST.get('email'))
            save_subscriber.save()
            return render(request, 'thanks.html')
    except Exception as e:
        Data_Logger.log_error_message(DJANGO_VIEWS.NEWS_LETTER, e, Data_Logger.get_client_ip(request))
        return redirect('error-404')
