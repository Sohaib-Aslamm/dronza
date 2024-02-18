from django.shortcuts import render
from home.models import userBlog
from dronzaPanel.models import SocialMedia, seoTags


def thankyou(request):
    return render(request, 'thanks.html')


def coming_soon(request):

    context = {
        'recent_blog_post': userBlog.objects.order_by('-sNo')[:2],
        'social_media': SocialMedia.objects.all(),
        'seo_tags': seoTags.objects.filter(page='coming_soon'),
    }
    return render(request, 'coming_soon.html', context)


def error_404(request):

    context = {
        'recent_blog_post': userBlog.objects.order_by('-sNo')[:2],
        'social_media': SocialMedia.objects.all(),
        'seo_tags': seoTags.objects.filter(page='error_404'),
    }
    return render(request, 'error_404.html', context)


def general_error(request):

    context = {
        'recent_blog_post': userBlog.objects.order_by('-sNo')[:2],
        'social_media': SocialMedia.objects.all(),
        'seo_tags': seoTags.objects.filter(page='general_error'),
    }
    return render(request, 'general_error.html', context)
