from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('django_admin', admin.site.urls, name="django_admin"),
    path('', include('dronzaPanel.urls')),
    path('', include('home.urls')),
    path('stripe/', include("djstripe.urls", namespace="djstripe")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
