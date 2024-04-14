"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.send_some_data),
    path('galleries/', views.get_all_galeries),
    path('galleries/<int:gallery_id>', views.get_gallery),
    path('galleries/<int:gallery_id>/userPermissions', views.get_user_permissions_to_gallery),
    path('galleries/<int:gallery_id>/pictures', views.get_all_pictures),
    path('pictures/<int:picture_id>', views.get_picture),
    path('pictures/<int:picture_id>/comments', views.get_all_comments),
    path('pictures/<int:picture_id>/rating', views.get_rating),
    path('pictures/<int:picture_id>/comments', views.get_user_permissions_to_gallery),
    path('user/<str:user_name>', views.get_user_info)
    
]
