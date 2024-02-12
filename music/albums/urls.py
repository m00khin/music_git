from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('albums', views.album_list, name='album_list'),
    path('albums/add', views.album_add, name='album_add'),
    path('albums/<int:pk>/edit', views.album_edit, name='album_edit'),
    path('albums/<int:pk>/delete', views.album_delete, name='album_delete'),
    path('albums/<int:pk>/remove', views.album_remove, name='album_remove'),
]
