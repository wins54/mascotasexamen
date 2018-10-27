from django.conf.urls import url
from . import views
from django.urls import path, include

urlpatterns = [

    path('', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^mascota/nueva/$', views.desempeno_nueva, name='desempeno_nueva'),
    url(r'^post/(?P<pk>\d+)/eliminar/$', views.post_remove1, name='post_remove1'),
    path('post/<int:pk>/edit/', views.desempeno_nueva1,
         name='post_desempeno_nueva1'),
    url(r'^mascota/nuevos/$', views.mascota_create, name='mascota_create'),


]
