from rest_framework import serializers
from .models import *

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'number']

class AlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ['id', 'title', 'songs', 'year']

class ArtistSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ['id', 'name', 'album']
