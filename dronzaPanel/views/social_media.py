from dronzaPanel.forms import SocialMediaForm
from dronzaPanel.models import SocialMedia

from django.shortcuts import render

from dronzaPanel.decorators import admin_only, custom_login_required


@custom_login_required
@admin_only
def adminsocial_media(request):
    if request.method == 'POST':
        SMFM = SocialMediaForm(request.POST, request.FILES)
        if SMFM.is_valid():
            EM = SMFM.cleaned_data['email']
            SK = SMFM.cleaned_data['skype']
            PH = SMFM.cleaned_data['phone']
            GIT = SMFM.cleaned_data['github']
            LIK = SMFM.cleaned_data['linkedin']
            GP = SMFM.cleaned_data['google_plus']
            YTB = SMFM.cleaned_data['youtube']
            FCBK = SMFM.cleaned_data['facebook']
            TWTR = SMFM.cleaned_data['twitter']
            reg = SocialMedia(email=EM, skype=SK, phone=PH, github=GIT, linkedin=LIK, google_plus=GP, youtube=YTB,
                              facebook=FCBK, twitter=TWTR)
            reg.save()
            SMFM = SocialMediaForm()
    else:
        SMFM = SocialMediaForm()
    SMdata = SocialMedia.objects.all()
    return render(request, 'adminSocialmedia.html', {'form': SMFM, 'SMdata': SMdata})