from django.urls import path, include
from rest_framework import routers
from . import views
from django.conf import settings
from django.conf.urls.static import static

###########################################################
################## Automatic URL mapping ##################
###########################################################
router = routers.DefaultRouter()
router.register('add_images', views.ImagesView, basename='images')
router.register('profile', views.UserProfileView)
router.register('show_all_images', views.UserImagesView, basename='user_images')


urlpatterns = [
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
