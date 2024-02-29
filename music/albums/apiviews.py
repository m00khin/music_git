# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import viewsets, filters
from .serializers import *


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    # permission_classes = (AllForAdminOtherReadOnly, )
    filter_backends = [filters.OrderingFilter]
    # search_fields = ['', '', '']


class SongsViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    # permission_classes = (AllForAdminOtherReadOnly, )
    filter_backends = [filters.OrderingFilter]
    # search_fields = ['', '', '']
