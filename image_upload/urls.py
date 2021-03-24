from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from image_upload.views import *

urlpatterns = [
    path('image_upload', image_view, name='image_upload'),
    path('success', success, name='success'),
    path('char_images', display_image_all, name='show_images'),
    path('last_image', display_last, name='last_image'),
    path('result',display_result,name='result'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
