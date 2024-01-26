from django.shortcuts import render, HttpResponseRedirect
from home.models import contact_us
from home.forms import contactForm
from dronzaPanel.models import SocialMedia, userBlog, seoTags, MainSlider
from home.definedEmails import notify_contact_us


def contactus(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            sv = contact_us.objects.create(name=name, subject=subject, email=email, phone=phone, message=message)
            notify_contact_us(name, email, message)  # Send email to the customer who contacted through the website
            return HttpResponseRedirect('/thank-you')
    else:
        form = contactForm()

    context = {
        'form': form,
        'recent_blog_post': userBlog.objects.order_by('-sNo')[:2],
        'social_media': SocialMedia.objects.all(),
        'seo_tags': seoTags.objects.filter(page='contact_us_page'),
        'SLIDER': MainSlider.objects.filter(page='contact_us_page'),
    }
    return render(request, 'contactUs.html', context)