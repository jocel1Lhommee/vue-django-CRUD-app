from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models

class Image(models.Model):
    img=models.ImageField(upload_to='post_img/',null=True,blank=True)
    name = models.CharField(max_length=50)
    alt = models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields='__all__'