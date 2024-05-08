# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
# from rest_framework import viewsets, filters, status
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .serializers import *


class AlbumsListView(APIView):
    # parser_classes = (FileUploadParser, MultiPartParser, FormParser)
    parser_classes = (MultiPartParser, FormParser)
    def get(self, request):
        queryset = Album.objects.all()
        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.FILES)
        print(request.data)
        serializer = AlbumSerializer(data=request.data)

        return Response({'received data': request.data})

        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class SongsDetailView(APIView):
    def get_object(self, pk):
        try:
            return Song.objects.filter(album_key=pk).values()
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        # queryset = Song.objects.filter(album_key=pk).values()
        queryset = self.get_object(pk)
        # serializer = SongDetailSerializer(queryset, many=True)
        serializer = SongSerializer(queryset, many=True)
        return Response(serializer.data)
        # return Response({'songs': serializer.data}, status=status.HTTP_200_OK)

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
