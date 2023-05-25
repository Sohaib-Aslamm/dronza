from django.shortcuts import render
from dronzaPanel.models import Gallery, SocialMedia, userBlog


def gallery(request):
    GLLRY = Gallery.objects.all()
    GLLRY2 = Gallery.objects.values('category').distinct()
    RCPST = userBlog.objects.order_by('-sNo')[:2]
    SMDT = SocialMedia.objects.all()
    context = {'GLLRY': GLLRY, 'GLLRY2': GLLRY2, 'RCPST': RCPST, 'SMDT': SMDT}
    return render(request, 'Gallery.html', context)