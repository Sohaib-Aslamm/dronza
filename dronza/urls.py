
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', include('dronzaPanel.urls')),
    path('', include('home.urls')),
    path('stripe/', include("djstripe.urls", namespace="djstripe")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
