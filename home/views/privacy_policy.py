from django.shortcuts import render
from dronzaPanel.models import PrivacyPolicy, SocialMedia, userBlog, seoTags, MainSlider


def privacy_policy(request):

    context = {
        'privacy_policy': PrivacyPolicy.objects.all(),
        'recent_blog_post': userBlog.objects.order_by('-sNo')[:2],
        'social_media': SocialMedia.objects.all(),
        'seo_tags': seoTags.objects.filter(page='privacy_policy_page'),
        'SLIDER': MainSlider.objects.filter(page='privacy_policy_page'),
    }
    return render(request, 'privacy_policy.html', context)
