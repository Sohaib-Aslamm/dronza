from dronzaPanel.forms import SEOTagsForm
from dronzaPanel.models import seoTags

from django.shortcuts import render

from dronzaPanel.decorators import admin_only, custom_login_required


@custom_login_required
@admin_only
def SEOTags(request):
    if request.method == 'POST':
        SEOFM = SEOTagsForm(request.POST, request.FILES)
        if SEOFM.is_valid():
            title = SEOFM.cleaned_data['title']
            page = SEOFM.cleaned_data['page']
            canonical = SEOFM.cleaned_data['canonical_link']
            description = SEOFM.cleaned_data['description']
            tags = SEOFM.cleaned_data['tags']
            reg = seoTags(title=title, page=page, canonical_link=canonical, description=description, tags=tags)
            reg.save()
            SEOFM = SEOTagsForm()
    else:
        SEOFM = SEOTagsForm()
    SEODATA = seoTags.objects.all()
    return render(request, 'seoTags.html', {'form': SEOFM, 'SEODATA': SEODATA})
