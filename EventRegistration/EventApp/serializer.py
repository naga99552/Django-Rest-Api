from rest_framework import serializers
from .models  import EventRegistration
from django.contrib.auth.models import User
from django.contrib.auth import login
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventRegistration()
        fields='__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
        kwargs={'password':{'write_only':True}}
    def create(self,validated_data):
        user=User(email=validated_data['email'],username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class AccountSeliazier(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,required=False)
    class Meta:
        model=EventRegistration
        fields='__all__'
    def creates(self,validated_data):
        return EventRegistration.objects.create_user(request_data=validated_data)


