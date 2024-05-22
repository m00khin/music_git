from django.urls import path
from . import apiviews


urlpatterns = [
    path('', apiviews.AlbumsListView.as_view()),
    path('<int:pk>/', apiviews.AlbumDetailView.as_view()),
    path('<int:pk>/songs/', apiviews.SongsListView.as_view()),
    path('<int:pk>/songs/<int:track>/', apiviews.SongDetailView.as_view()),
]
