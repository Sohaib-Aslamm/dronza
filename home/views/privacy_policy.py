from django.shortcuts import render, redirect
from dronzaPanel.models import PrivacyPolicy, SocialMedia, userBlog, seoTags, MainSlider
from home.commands import Data_Logger
from home.enumerators import DJANGO_VIEWS


def privacy_policy(request):
    try:
        context = {
            'privacy_policy': PrivacyPolicy.objects.all(),
            'recent_blog_post': userBlog.objects.order_by('-sNo')[:2],
            'social_media': SocialMedia.objects.all(),
            'seo_tags': seoTags.objects.filter(page='privacy_policy_page'),
            'SLIDER': MainSlider.objects.filter(page='privacy_policy_page'),
        }
        return render(request, 'privacy_policy.html', context)
    except Exception as e:
        Data_Logger.log_error_message(DJANGO_VIEWS.PRIVACY_POLICY, e, Data_Logger.get_client_ip(request))
        return redirect('bad-request')

