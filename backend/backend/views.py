# django-react-docker/backend/backend/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
@api_view(['GET'])
def send_some_data(request):
    return JsonResponse({
        'data': 'Hello from django backend'
    })
