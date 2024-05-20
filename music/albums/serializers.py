from rest_framework import serializers
from .models import *


class AlbumSerializer(serializers.ModelSerializer):
    # picture = serializers.FileField()
    class Meta:
        model = Album
        # fields = ['id', 'artist', 'name', 'year', 'maker']
        fields = '__all__'


# class CoverSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Album
#         fields = ['cover']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        # fields = ['track_no', 'track_name', 'track_artist', 'track_time']
        exclude = ['id', 'album_key']


class AlbumDetailSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        # fields = ['id', 'artist', 'name', 'year', 'maker', 'cover', 'songs']
        fields = ['id', 'artist', 'name', 'year', 'maker', 'songs']
        depth = 1
