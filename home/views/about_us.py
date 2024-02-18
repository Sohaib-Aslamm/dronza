from django.shortcuts import render, redirect
from dronzaPanel.models import AboutTitlePost, QualityTrust, OurTeam, SocialMedia, userBlog, seoTags, MainSlider
from home.commands import Data_Logger
from home.enumerators import DJANGO_VIEWS


def about(request):
    try:
        context = {
            'about_title_post': AboutTitlePost.objects.all(),
            'quality_trust': QualityTrust.objects.all(),
            'our_team': OurTeam.objects.all(),
            'recent_blog_post': userBlog.objects.order_by('-sNo')[:2],
            'social_media': SocialMedia.objects.all(),
            'seo_tags': seoTags.objects.filter(page='about_page'),
            'main_slider': MainSlider.objects.filter(page='about_page')
        }
        return render(request, 'About.html', context)
    except Exception as e:
        Data_Logger.log_error_message(DJANGO_VIEWS.USER_REGISTER, e, Data_Logger.get_client_ip(request))
        return redirect('bad-request')
