from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('albums', views.album_list, name='album_list'),
    path('albums/create', views.album_create, name='album_create'),
    path('albums/update/<int:pk>', views.album_update, name='album_update'),
    path('albums/delete/<int:pk>', views.album_delete, name='album_delete'),
    path('albums/remove/<int:pk>', views.album_remove, name='album_remove'),
    path('albums/<int:pk>/tracks', views.album_tracks, name='album_tracks'),
]
# path('albums/song/add', views.add_tracks, name='add_tracks'),
