from dronzaPanel.forms import HomeSRFPForm, WhatPeopleSForm, OurPartnerForm, OurTeamForm
from dronzaPanel.models import HomeSRFP, WhatPeopleSay, OurPartner, OurTeam


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dronzaPanel.decorators import admin_only


@login_required(login_url='/user-login')
@admin_only
def adminHomeSRFP(request):
    if request.method == 'POST':
        SRFPFM = HomeSRFPForm(request.POST, request.FILES)
        if SRFPFM.is_valid():
            SC = SRFPFM.cleaned_data['satisfied_clients']
            RS = SRFPFM.cleaned_data['resolution']
            FT = SRFPFM.cleaned_data['flight_time']
            PD = SRFPFM.cleaned_data['project_done']
            reg = HomeSRFP(satisfied_clients=SC, resolution=RS, flight_time=FT, project_done=PD)
            reg.save()
            SRFPFM = HomeSRFPForm()
    else:
        SRFPFM = HomeSRFPForm()
    SRFPDT = HomeSRFP.objects.all()
    return render(request, 'adminHomeSRFP.html', {'form': SRFPFM, 'SRFPDT': SRFPDT})


@login_required(login_url='/user-login')
@admin_only
def adminPeopleSay(request):
    if request.method == 'POST':
        WPSFM = WhatPeopleSForm(request.POST, request.FILES)
        if WPSFM.is_valid():
            NM = WPSFM.cleaned_data['name']
            DESG = WPSFM.cleaned_data['designation']
            SAY = WPSFM.cleaned_data['say_something']
            ICN = WPSFM.cleaned_data['icon']
            reg = WhatPeopleSay(name=NM, designation=DESG, say_something=SAY, icon=ICN)
            reg.save()
            WPSFM = WhatPeopleSForm()
    else:
        WPSFM = WhatPeopleSForm()
    WPSDT = WhatPeopleSay.objects.all()
    return render(request, 'adminPeopleSay.html', {'form': WPSFM, 'WPSDT': WPSDT})


@login_required(login_url='/user-login')
@admin_only
def adminOurPartner(request):
    if request.method == 'POST':
        OPTFM = OurPartnerForm(request.POST, request.FILES)
        if OPTFM.is_valid():
            CN = OPTFM.cleaned_data['company_name']
            DESC = OPTFM.cleaned_data['description']
            LOGO = OPTFM.cleaned_data['logo']
            reg = OurPartner(company_name=CN, description=DESC, logo=LOGO)
            reg.save()
            OPTFM = OurPartnerForm()
    else:
        OPTFM = OurPartnerForm()
    OPTDT = OurPartner.objects.all()
    return render(request, 'adminOurPartner.html', {'form': OPTFM, 'OPTDT': OPTDT})


@login_required(login_url='/user-login')
@admin_only
def adminOurTeam(request):
    if request.method == 'POST':
        OUTFM = OurTeamForm(request.POST, request.FILES)
        if OUTFM.is_valid():
            NM = OUTFM.cleaned_data['name']
            EML = OUTFM.cleaned_data['email']
            PHN = OUTFM.cleaned_data['phone']
            EXPR = OUTFM.cleaned_data['experience']
            DSG = OUTFM.cleaned_data['designation']
            SM1 = OUTFM.cleaned_data['socialmedia1']
            SM2 = OUTFM.cleaned_data['socialmedia2']
            SM3 = OUTFM.cleaned_data['socialmedia3']
            DESC = OUTFM.cleaned_data['description']
            PRF = OUTFM.cleaned_data['profile']
            reg = OurTeam(name=NM, email=EML, phone=PHN, designation=DSG, experience=EXPR, socialmedia1=SM1,
                          socialmedia2=SM2, socialmedia3=SM3, description=DESC, profile=PRF)
            reg.save()
            OUTFM = OurTeamForm()
    else:
        OUTFM = OurTeamForm()
    data = OurTeam.objects.all()
    return render(request, 'adminOurTeam.html', {'form': OUTFM, 'OUTdata': data})