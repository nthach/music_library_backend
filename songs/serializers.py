from dataclasses import field
from pickle import SHORT_BINSTRING
from rest_framework import serializers
from .models import App, Song


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'make', 'model', 'year', 'price']