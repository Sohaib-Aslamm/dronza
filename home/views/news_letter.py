from django.shortcuts import render
from home.models import NewsLetterSubscriber


def news_letter_subscriber(request):
    if request.method == 'POST':
        save_subscriber = NewsLetterSubscriber(email=request.POST.get('email'))
        save_subscriber.save()
        return render(request, 'thanks.html')
