from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('album', views.album_list, name='album_list'),
    path('album/add', views.album_create, name='album_create'),
    path('album/<int:pk>/change', views.album_update, name='album_update'),
    path('album/<int:pk>/delete', views.album_delete, name='album_delete'),
    path('album/<int:pk>/remove', views.album_remove, name='album_remove'),
    path('album/<int:pk>/tracks', views.album_tracks, name='album_tracks'),
    path('album/<int:pk>/content', views.tracks_load, name='track_loader'),
    path('album/<int:pk>/tracks/add', views.create_track, name='track_create'),
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
