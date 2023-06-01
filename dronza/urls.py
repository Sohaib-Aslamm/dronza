from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    path('django_admin', admin.site.urls, name="django_admin"),
    path('', RedirectView.as_view(url='https://dronza.org', permanent=True)),
    path('', include('dronzaPanel.urls')),
    path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
