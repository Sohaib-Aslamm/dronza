from django.shortcuts import render
from dronzaPanel.models import AboutTitlePost, QualityTrust, OurTeam, SocialMedia, userBlog, seoTags, MainSlider


def about(request):
    context = {
        'about_title_post': AboutTitlePost.objects.all(),
        'quality_trust': QualityTrust.objects.all(),
        'our_team': OurTeam.objects.all(),
        'RCPST': userBlog.objects.order_by('-sNo')[:2],
        'social_media': SocialMedia.objects.all(),
        'seo_tags': seoTags.objects.filter(page='about_page'),
        'main_slider': MainSlider.objects.filter(page='about_page')
    }
    return render(request, 'About.html', context)
