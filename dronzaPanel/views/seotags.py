from dronzaPanel.forms import SEOTagsForm
from dronzaPanel.models import seoTags

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dronzaPanel.decorators import admin_only


@login_required(login_url='/user_login')
@admin_only
def SEOTags(request):
    if request.method == 'POST':
        SEOFM = SEOTagsForm(request.POST, request.FILES)
        if SEOFM.is_valid():
            title = SEOFM.cleaned_data['title']
            page = SEOFM.cleaned_data['page']
            description = SEOFM.cleaned_data['description']
            tags = SEOFM.cleaned_data['tags']
            reg = seoTags(title=title, page=page, description=description, tags=tags)
            reg.save()
            SEOTagsForm()
    else:
        SEOFM = SEOTagsForm()
    SEODATA = seoTags.objects.all()
    return render(request, 'seoTags.html', {'form': SEOFM, 'SEODATA': SEODATA})
