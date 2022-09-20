from dataclasses import field
from pickle import SHORT_BINSTRING
from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'release', 'genre']