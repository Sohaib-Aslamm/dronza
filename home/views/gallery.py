from django.shortcuts import render, redirect
from dronzaPanel.models import Gallery, SocialMedia, userBlog, seoTags, MainSlider
from home.commands import Data_Logger
from home.enumerators import DJANGO_VIEWS


def gallery(request):
    try:
        context = {
            'gallery': Gallery.objects.all(),
            'categories': Gallery.objects.values('category').distinct(),
            'recent_blog_post': userBlog.objects.order_by('-sNo')[:2],
            'social_media': SocialMedia.objects.all(),
            'seo_tags': seoTags.objects.filter(page='gallery_page'),
            'SLIDER':  MainSlider.objects.filter(page='gallery_page'),
        }
        return render(request, 'Gallery.html', context)
    except Exception as e:
        Data_Logger.log_error_message(DJANGO_VIEWS.GALLERY, e, Data_Logger.get_client_ip(request))
        return redirect('bad-request')
