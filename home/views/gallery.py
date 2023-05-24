from django.shortcuts import render
from dronzaPanel.models import Gallery, SocialMedia, userBlog


def gallery(request):
    GLLRY = Gallery.objects.all()
    GLLRY2 = Gallery.objects.values('category').distinct()
    RCPST = userBlog.objects.all().order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    latest_keywords = userBlog.objects.order_by('-sNo').values_list('tags', flat=True)[:3]
    context = {'GLLRY': GLLRY, 'GLLRY2': GLLRY2, 'RCPST': RCPST, 'SMDT': SMDT, 'latest_keywords': latest_keywords}
    return render(request, 'Gallery.html', context)