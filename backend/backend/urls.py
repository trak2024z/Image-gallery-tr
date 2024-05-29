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
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("test/", TestEndpointView.as_view(), name="test"),
    path("galleries/", AllGalleriesAPIView.as_view(), name="all-galleries"),
    path("galleries/<int:gallery_id>", GalleryDetailView.as_view(), name="gallery-detail"),
    path(
        "galleries/<int:gallery_id>/userPermissions",
        UserPermGalView.as_view(), name="user-permision-to-gallery",
    ),
    path("galleries/<int:gallery_id>/pictures", GalleryPicturesAPIView.as_view(), name="all-pictures"),
    path("pictures/<int:picture_id>", ImageDetailView.as_view(), name="image-detail"),
    path("pictures/<int:picture_id>/comments", AllCommentsView.as_view(), name="comments-for-picture"),
    path("pictures/<int:picture_id>/rating", RatingView.as_view(), name="ratings-for-picture"),
    path("user/<str:user_name>", UserInfoView.as_view(), name="user-info"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('gallery/', CreateGalleryView.as_view(), name='create-gallery'),
    path('galleries/<int:pk>/picture/', AddPictureView.as_view(), name='add-picture'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
