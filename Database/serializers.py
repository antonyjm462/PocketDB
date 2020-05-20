from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Database

class DatabaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Database
        # fields = ['_id','_data','created_at','updated_at']
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']