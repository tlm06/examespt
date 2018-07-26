from .models import Platform, Game, Player, Videogame
from rest_framework import serializers


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'mail', 'first_name', 'last_name', 'pc_gamer_tag', 'ps4_gamer_tag', 'xbox_gamer_tag')


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ('id', 'name')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('platform', 'videogame', 'created_by', 'opponent', 'has_started', 'winner')



