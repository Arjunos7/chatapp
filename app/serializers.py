from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile,Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['profile_image']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']

    def create(self, validated_data):
        user=User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'])

class UserDetailSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer()

    class Meta:
        model=User
        fields=['id','username','profile']

class MessageSerializer(serializers.ModelSerializer):
    replies=serializers.SerializerMethodField()

    class Meta:
        model=Message
        fields=['id','sender','receiver','text','created_at','parent_message','replies']

    def get_replies(self,obj):
        replies=Message.objects.filter(parent_message=obj)
        return MessageSerializer(replies,many=True).data





class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['receiver', 'text', 'parent_message']

    def create(self, validated_data):
        validated_data['sender'] = self.context['request'].user
        return super().create(validated_data)

