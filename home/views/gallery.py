from django.shortcuts import render
from dronzaPanel.models import Gallery, SocialMedia, userBlog, seoTags, MainSlider


def gallery(request):
    GLLRY = Gallery.objects.all()
    GLLRY2 = Gallery.objects.values('category').distinct()
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    SEOTAGS = seoTags.objects.filter(page='gallery_page')
    SLIDER = MainSlider.objects.filter(page='gallery_page')
    context = {'GLLRY': GLLRY, 'GLLRY2': GLLRY2, 'RCPST': RCPST, 'SMDT': SMDT, 'SEOTAGS': SEOTAGS, 'SLIDER': SLIDER}
    return render(request, 'Gallery.html', context)