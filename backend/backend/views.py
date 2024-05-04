# django-react-docker/backend/backend/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny
@api_view(['GET'])
def send_some_data(request):
    return JsonResponse({
        'data': 'Hello from django backend'
    })

@api_view(['GET'])
def get_all_galeries(request):
    return JsonResponse(
        {
            'galeries':'All galleries'
        })
    
@api_view(['GET'])
def get_gallery(request, gallery_id):
    return JsonResponse(
        {
            'galery':'Gallery with id: ' + str(gallery_id)
        })

@api_view(['GET'])
def get_all_pictures(request, gallery_id):
    return JsonResponse(
        {
            'pictures':'All pictures'
        })

@api_view(['GET'])
def get_picture(request, picture_id):
    return JsonResponse(
        {
            'pictures':'Picture with id: ' + str(picture_id)
        })

@api_view(['GET'])
def get_all_comments(request, picture_id):
    return JsonResponse(
        {
            'comments':'All comments at picture with id: ' + str(picture_id)
        })

@api_view(['GET'])
def get_rating(request, picture_id):
    return JsonResponse(
        {
            'rating':'Rating at picture with id: ' + str(picture_id)
        })

@api_view(['GET'])
def get_user_info(request, user_name):
    return JsonResponse(
        {
            'user':'Info of user with name: ' + user_name
        })
    
@api_view(['GET'])
def get_user_permissions_to_gallery(request, gallery_id):
    return JsonResponse(
        {
            'users':'Users with permission to gallery'
        })

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
