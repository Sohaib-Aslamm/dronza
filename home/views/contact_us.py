from django.shortcuts import render, HttpResponseRedirect
from home.models import contact_us
from home.forms import contactForm
from dronzaPanel.models import SocialMedia, userBlog, seoTags
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
            return HttpResponseRedirect('/thankyou')
    else:
        form = contactForm()

    SMDT = SocialMedia.objects.all()
    SEOTAGS = seoTags.objects.filter(page='contact_us_page')
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    context = {
        'form': form,
        'RCPST': RCPST,
        'SMDT': SMDT,
        'SEOTAGS': SEOTAGS
    }
    return render(request, 'contactUs.html', context)