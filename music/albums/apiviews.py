# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .serializers import *


class AlbumsListView(APIView):
    def get(self, request):
        queryset = Album.objects.all()
        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumDetailView(APIView):
    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = AlbumSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = self.get_object(pk)
        serializer = AlbumSerializer(queryset, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SongsListView(APIView):
    def get_object(self, pk):
        try:
            return Song.objects.filter(album_key=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = SongSerializer(queryset, many=True)
        return Response({'songs': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SongDetailView(APIView):
    def get_object(self, pk, track):
        try:
            return Song.objects.get(album_key=pk, track_no=track)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk, track):
        queryset = self.get_object(pk, track)
        serializer = SongSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk, track):
        queryset = self.get_object(pk, track)
        serializer = SongSerializer(queryset, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, track):
        queryset = self.get_object(pk, track)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
