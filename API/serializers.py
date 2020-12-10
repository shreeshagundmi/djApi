# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Crud_Users
#

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crud_Users
        fields = '__all__'