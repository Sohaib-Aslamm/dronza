from django.shortcuts import render
from dronzaPanel.models import PrivacyPolicy, SocialMedia, userBlog, seoTags, MainSlider


def privacy_policy(request):
    policy = PrivacyPolicy.objects.all()
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    SEOTAGS = seoTags.objects.filter(page='privacy_policy_page')
    SLIDER = MainSlider.objects.filter(page='privacy_policy_page')
    context = {'policy': policy, 'RCPST': RCPST, 'SMDT': SMDT, 'SEOTAGS': SEOTAGS, 'SLIDER': SLIDER}
    return render(request, 'privacy_policy.html', context)
