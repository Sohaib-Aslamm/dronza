from django.shortcuts import render, HttpResponseRedirect
from home.models import contact_us
from home.forms import contactForm
from dronzaPanel.models import SocialMedia, userBlog
from home.definedEmails import notify_contact_us


def contactus(request):
    if request.method == 'POST':
        CNTCTFM = contactForm(request.POST, request.FILES)
        if CNTCTFM.is_valid():
            NM = CNTCTFM.cleaned_data['name']
            SBJ = CNTCTFM.cleaned_data['subject']
            EM = CNTCTFM.cleaned_data['email']
            PH = CNTCTFM.cleaned_data['phone']
            MSG = CNTCTFM.cleaned_data['message']
            sv = contact_us(name=NM, subject=SBJ, email=EM, phone=PH, message=MSG)
            sv.save()
            notify_contact_us(NM, EM, MSG)  # send email to customer who contacted by web site
            contactForm()
            return HttpResponseRedirect('/thankyou')
    else:
        CNTCTFM = contactForm()
        SMDT = SocialMedia.objects.all()
        RCPST = userBlog.objects.all().order_by('-sNo')[:2]
        context = {'form': CNTCTFM, 'RCPST': RCPST, 'SMDT': SMDT}
    return render(request, 'contactUs.html', context)
