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
    path('<int:pk>/tracks/', apiviews.SongsDetailView.as_view()),
]

"""
    path('', view) - albums(get) + add album(post)

    path('<int:pk>/', view) - read album (with tracks)
    path('<int:pk>/update', view) - update album
    path('<int:pk>/delete', view) - delete album
    path('<int:pk>/tracks', view) - album tracks
    path('<int:pk>/tracks/add', view) - add track
"""
# path('', include(router.urls)),
