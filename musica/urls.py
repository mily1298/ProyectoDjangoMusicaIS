from django.contrib import admin
from django.urls import include, path

from musica import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('top-songs', views.TopSongs.as_view(), name='top-songs')
 ]