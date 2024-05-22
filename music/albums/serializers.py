from rest_framework import serializers
from .models import *


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        exclude = ['cover']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        # exclude = ['id', 'album_key']
        fields = '__all__'
