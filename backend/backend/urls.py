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
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("test/", views.TestEndpointView.as_view(), name="test"),
    path("galleries/", views.AllGalleriesAPIView.as_view(), name="all-galleries"),
    path("galleries/<int:gallery_id>", views.GalleryDetailView.as_view(), name="gallery-detail"),
    path(
        "galleries/<int:gallery_id>/userPermissions",
        views.UserPermGalView.as_view(), name="user-permision-to-gallery",
    ),
    path("galleries/<int:gallery_id>/pictures", views.GalleryPicturesAPIView.as_view(), name="all-pictures"),
    path("pictures/<int:picture_id>", views.ImageDetailView.as_view(), name="image-detail"),
    path("pictures/<int:picture_id>/comments", views.AllCommentsView.as_view(), name="comments-for-picture"),
    path("pictures/<int:picture_id>/rating", views.RatingView.as_view(), name="ratings-for-picture"),
    path("user/<str:user_name>", views.UserInfoView.as_view(), name="user-info"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
