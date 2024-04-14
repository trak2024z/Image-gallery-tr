# django-react-docker/backend/backend/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
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