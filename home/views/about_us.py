from django.shortcuts import render
from dronzaPanel.models import AboutTitlePost, QualityTrust, OurTeam, SocialMedia, userBlog


def about(request):
    TTDATA = AboutTitlePost.objects.all()
    QTDATA = QualityTrust.objects.all()
    TMDATA = OurTeam.objects.all()
    SMDT = SocialMedia.objects.all()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    latest_keywords = userBlog.objects.order_by('-sNo').values_list('tags', flat=True)[:3]
    context = {'TTDATA': TTDATA, 'QTDATA': QTDATA, 'TMDATA': TMDATA, 'RCPST': RCPST, 'SMDT': SMDT,
               'latest_keywords': latest_keywords}
    return render(request, 'About.html', context)
