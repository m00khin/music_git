# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404, JsonResponse
from .serializers import *


class AlbumsListView(APIView):
    # parser_classes = (FileUploadParser, MultiPartParser, FormParser)
    # parser_classes = (MultiPartParser, FormParser)
    parser_classes = (MultiPartParser, )

    def get(self, request):
        queryset = Album.objects.all()
        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data)

# """
# https://stackoverflow.com/questions/46965670/how-to-use-multipartparser-in-django-rest-framework
# """
    def post(self, request):
        # print(request.FILES['cover'])
        # print(request.data)
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # print(serializer.data)
            # serializer.save()
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
        serializer = AlbumDetailSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = self.get_object(pk)
        serializer = AlbumDetailSerializer(queryset, data=request.data)
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
            return Song.objects.filter(album_key=pk).values()
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = SongSerializer(queryset, many=True)
        # return Response(serializer.data)
        return Response({'songs': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, pk):
        pass


class SongsDetailView(APIView):
    def get_object(self, pk, track):
        try:
            return Song.objects.filter(album_key=pk, track_no=track).values()
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk, track):
        queryset = self.get_object(pk, track)
        serializer = SongSerializer(queryset, many=True)
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

# class AlbumViewSet(viewsets.ModelViewSet):
#     queryset = Album.objects.all()
#     serializer_class = AlbumSerializer
#     # permission_classes = (AllForAdminOtherReadOnly, )
#     filter_backends = [filters.OrderingFilter]
#     # search_fields = ['', '', '']
#     # http_method_names = ['get']
#
#
# class SongsViewSet(viewsets.ModelViewSet):
#     queryset = Song.objects.all()
#     serializer_class = SongSerializer
#     # permission_classes = (AllForAdminOtherReadOnly, )
#     filter_backends = [filters.OrderingFilter]
#     # search_fields = ['', '', '']
