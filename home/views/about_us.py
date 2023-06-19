from django.shortcuts import render
from dronzaPanel.models import AboutTitlePost, QualityTrust, OurTeam, SocialMedia, userBlog, seoTags, MainSlider


def about(request):
    TTDATA = AboutTitlePost.objects.all()
    QTDATA = QualityTrust.objects.all()
    TMDATA = OurTeam.objects.all()
    SMDT = SocialMedia.objects.all()
    SEOTAGS = seoTags.objects.filter(page='about_page')
    SLIDER = MainSlider.objects.filter(page='about_page')
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    context = {'TTDATA': TTDATA, 'QTDATA': QTDATA, 'TMDATA': TMDATA, 'RCPST': RCPST, 'SMDT': SMDT, 'SEOTAGS': SEOTAGS,
               'SLIDER': SLIDER}
    return render(request, 'About.html', context)
