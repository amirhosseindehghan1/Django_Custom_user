from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from Account.serializer import MyUserSerializer, CreateMyUserSerializer
from Account.models import MyUser
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password

class MyUserView(APIView):
    def get(self, request):
        all_user_obj = MyUser.objects.all()
        serializer = MyUserSerializer(all_user_obj, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = CreateMyUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data.get('password')
        hashed_password = make_password(password)
        serializer.validated_data['password'] = hashed_password
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request,id):
        user_profile_obj = MyUser.objects.get(id=id)
        serializer = MyUserSerializer(instance=user_profile_obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self, request, id):
        user_profile_object = MyUser.objects.get(id=id)
        user_profile_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)