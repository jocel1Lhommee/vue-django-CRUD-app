

# Create your views here.


from unicodedata import name
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


from .models.image import Image, ImageSerializer

@api_view(http_method_names=["GET"])
def Image_detail(request:Request,image_name:str):
    if request.method == 'GET' :
        image=Image.objects.get(name=image_name)
        serializer = ImageSerializer(instance=image)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    return Response(data="Image pas trouvé", status=status.HTTP_404_NOT_FOUND)