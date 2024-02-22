from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('albums', views.album_list, name='album_list'),
    path('albums/add', views.album_create, name='album_create'),
    path('albums/album/<int:pk>/change', views.album_update, name='album_update'),
    path('albums/album/<int:pk>/delete', views.album_delete, name='album_delete'),
    path('albums/album/<int:pk>/remove', views.album_remove, name='album_remove'),
    path('albums/album/<int:pk>/tracks', views.album_tracks, name='album_tracks'),
    path('albums/album/<int:pk>/content', views.tracks_load, name='track_loader'),
    path('albums/album/<int:pk>/song/add', views.tracks_add, name='track_create'),
]
#
#path('albums/song/add', views.create_track, name='track_create'),
#
# path('albums/song/<int:pk>/change', views.add_tracks, name='add_tracks'),
# path('albums/song/<int:pk>/delete', views.add_tracks, name='add_tracks'),

# path('albums', views.album_list, name='album_list'),
# path('albums/create', views.album_create, name='album_create'),
# path('albums/update/<int:pk>', views.album_update, name='album_update'),
# path('albums/delete/<int:pk>', views.album_delete, name='album_delete'),
# path('albums/remove/<int:pk>', views.album_remove, name='album_remove'),
# path('albums/<int:pk>/tracks', views.album_tracks, name='album_tracks'),
