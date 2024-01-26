from django.shortcuts import render
from home.models import userBlog
from dronzaPanel.models import SocialMedia, seoTags, MainSlider


def thankyou(request):
    return render(request, 'thanks.html')


def coming_soon(request):

    context = {
        'recent_blog_post': userBlog.objects.order_by('-sNo')[:2],
        'social_media': SocialMedia.objects.all(),
        'seo_tags': seoTags.objects.filter(page='coming_soon'),
        'SLIDER': MainSlider.objects.filter(page='coming_soon_page'),
    }
    return render(request, 'error404.html', context)
