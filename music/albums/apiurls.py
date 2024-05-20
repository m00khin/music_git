# from rest_framework.routers import DefaultRouter
# from django.urls import path, include
from django.urls import path
from . import apiviews
from .apiviews import *


# router = DefaultRouter()
# router.register(r'album', AlbumViewSet)
# router.register(r'song', SongsViewSet)
# router.register(r'song/xxxx/', SongsViewSet)

urlpatterns = [
    path('', apiviews.AlbumsListView.as_view()),
    path('<int:pk>/', apiviews.AlbumDetailView.as_view()),
    path('<int:pk>/songs/', apiviews.SongsListView.as_view()),
    path('<int:pk>/songs/<int:track>/', apiviews.SongsDetailView.as_view()),
]

"""
    path('', view) - albums(get) + add album(post)
    path('<int:pk>/', view) - read(get) album (with songs)
    path('<int:pk>/update', view) - update album(put)
    path('<int:pk>/delete', view) - delete album(delete) with songs
    
    path('<int:pk>/songs', view) - songs(get, post) 
    path('<int:pk>/songs/<int:track>', view) - song(get, put, delete)
"""
# path('', include(router.urls)),
