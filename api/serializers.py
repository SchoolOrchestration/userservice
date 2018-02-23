from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Team


class UserLogin(object):
    def __init__(self, username="", password=""):
        self.password = password
        self.username = username


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128, required=True)
    password = serializers.CharField(max_length=128, required=True)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        return instance

    def create(self, validated_data):
        return UserLogin(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    teams = serializers.SerializerMethodField()

    class Meta:
        model = User
        depth = 1
        fields = ('username', 'id', 'teams')

    @staticmethod
    def get_teams(user):
        team_name_array = []
        for team in user.team_set.all():
            team_name_array.append(team.name)
        return team_name_array
