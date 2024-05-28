from django.db import models
from django.contrib.auth.models import User


class Gallery(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    path = models.ImageField(upload_to='images/')
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.CharField(max_length=1024)
    date = models.DateField(auto_now_add=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Rating(models.Model):
    like = models.BooleanField(default=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class GalleryPermission(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
