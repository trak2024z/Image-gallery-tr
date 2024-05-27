# django-react-docker/backend/backend/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from .models import Image, Gallery


class TestEndpointView(APIView):
    def get(self, request):
        return Response({"data": "Hello from django backend"})


class AllCommentsView(APIView):
    def get(self, request, picture_id):
        return Response({"comments": "All comments at picture with id: " + str(picture_id)})


class RatingView(APIView):
    def get(self, request, picture_id):
        return Response({"rating": "Rating at picture with id: " + str(picture_id)})


class UserInfoView(APIView):
    def get(self, request, user_name):
        return Response({"user": "Info of user with name: " + user_name})


class UserPermGalView(APIView):
    def get(self, request, gallery_id):
        return Response({"users": "Users with permission to gallery"})
    

class RegisterView(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            return Response(
                {"message": "Jesteś już zalogowany"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            user_data = UserSerializer(user).data
            return Response(
                {"token": token.key, "user": user_data}, status=status.HTTP_201_CREATED
            )
        return Response(
            {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class LoginView(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            return Response(
                {"message": "Jesteś już zalogowany"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data["username"],
                password=serializer.validated_data["password"],
            )
            if user:
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                user_data = UserSerializer(user).data
                return Response(
                    {"token": token.key, "user": user_data}, status=status.HTTP_200_OK
                )
            return Response(
                {"message": "Nieprawidłowy login lub hasło"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ImageDetailView(APIView):
    def get(self, request, picture_id):
        try:
            photo = Image.objects.get(pk=picture_id)
            serializer = ImageSerializer(photo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Image.DoesNotExist:
            return Response({"details": "Image not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, picture_id):
        try:
            photo = Image.objects.get(pk=picture_id)
            photo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Image.DoesNotExist:
            return Response({"details": "Image not found."}, status=status.HTTP_404_NOT_FOUND)


class GalleryDetailView(APIView):
    def get(self, request, gallery_id):
        try:
            gallery = Gallery.objects.get(pk=gallery_id)
            serializer = GallerySerializer(gallery)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Gallery.DoesNotExist:
            return Response({"details": "Gallery not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, gallery_id):
        try:
            gallery = Gallery.objects.get(pk=gallery_id)
            gallery.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Gallery.DoesNotExist:
            return Response({"details": "Gallery not found."}, status=status.HTTP_404_NOT_FOUND)
        
        
class GalleryPicturesAPIView(APIView):
    def get(self, request, gallery_id):
        try:
            gallery = Gallery.objects.get(pk=gallery_id)
        except Gallery.DoesNotExist:
            return Response({'details': 'Gallery not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = GalleryImageSerializer(gallery)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AllGalleriesAPIView(APIView):
    def get(self, request):
        galleries = Gallery.objects.all()
        serializer = GallerySerializer(galleries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)