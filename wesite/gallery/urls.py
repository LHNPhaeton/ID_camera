from django.urls import path
from .upload import upload_image
from . import views
#url(r'^upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
urlpatterns = [
    path('upload/', upload_image, name = 'upload_image'),
    #path('about/', views.about, name='about'),
    #path('typography/', views.typography, name='typography'),
    #path('gallery/', views.gallery, name='gallery'),
    #path('contact/', views.contact, name='contact'),
]