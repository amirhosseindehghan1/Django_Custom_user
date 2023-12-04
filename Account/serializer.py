from rest_framework import serializers
from Account.models import MyUser

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'


class CreateMyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields =['email', 'first_name', 'last_name', 'mobile', 'password']