from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'camposApp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^guardar/', views.guardarIndex, name='guardar'),
    url(r'^secundaria/', views.secundaria, name='secundaria'),
    url(r'^final/', views.final, name='final'),
]
