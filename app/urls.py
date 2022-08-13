from . import views
from django.urls import path
from django.conf import settings #add this
from django.conf.urls.static import static 
urlpatterns = [
    path('', views.UploadImage, name='UploadImage'),
    path('output/', views.output, name='output'),


]

