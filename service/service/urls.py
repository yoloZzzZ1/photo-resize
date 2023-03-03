from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView
from photos.urls import urlpatterns as photos_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
]

urlpatterns += photos_urls