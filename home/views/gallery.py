from django.shortcuts import render
from dronzaPanel.models import Gallery, SocialMedia, userBlog, seoTags, MainSlider


def gallery(request):

    context = {
        'gallery': Gallery.objects.all(),
        'categories': Gallery.objects.values('category').distinct(),
        'recent_blog_post': userBlog.objects.order_by('-sNo')[:2],
        'social_media': SocialMedia.objects.all(),
        'seo_tags': seoTags.objects.filter(page='gallery_page'),
        'SLIDER':  MainSlider.objects.filter(page='gallery_page'),
    }
    return render(request, 'Gallery.html', context)
