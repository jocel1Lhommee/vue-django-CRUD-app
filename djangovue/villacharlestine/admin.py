from django.contrib import admin

# Register your models here.
from .models.image import Image
admin.site.register(Image)