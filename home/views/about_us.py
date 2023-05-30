from django.shortcuts import render
from dronzaPanel.models import AboutTitlePost, QualityTrust, OurTeam, SocialMedia, userBlog, seoTags


def about(request):
    TTDATA = AboutTitlePost.objects.all()
    QTDATA = QualityTrust.objects.all()
    TMDATA = OurTeam.objects.all()
    SMDT = SocialMedia.objects.all()
    SEOTAGS = seoTags.objects.all()
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    context = {'TTDATA': TTDATA, 'QTDATA': QTDATA, 'TMDATA': TMDATA, 'RCPST': RCPST, 'SMDT': SMDT, 'SEOTAGS': SEOTAGS}
    return render(request, 'About.html', context)
