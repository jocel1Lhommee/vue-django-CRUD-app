from django.urls import path
from . import views
urlpatterns =[
    path('image/<str:image_name>', views.Image_detail,name = "Image_detail")
]