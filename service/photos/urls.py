from django.urls import path, include
from rest_framework.routers import DefaultRouter
from photos.views.photos import PhotoViewSet

router = DefaultRouter()

router.register(r'', PhotoViewSet, 'positions')


urlpatterns = [
    path('file/', include(router.urls)),
]