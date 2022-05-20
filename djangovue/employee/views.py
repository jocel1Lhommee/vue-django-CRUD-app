from django import http
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Employee
from .serializers import EmployeeSerializer

@api_view(http_method_names=["POST"])
# Create your views here.
def homepage(request:Request):
    if request.method == "POST":
        data= request.data
        response={"message":"Hello World", "data": data}
        return Response(data=response, status=status.HTTP_201_CREATED)
    return Response(data=response, status=status.HTTP_200_OK)

@api_view(http_method_names=["GET","POST"])
def ListEmployee(request:Request):
    if request.method == 'GET' :
        employees= Employee.objects.all()
        serializer = EmployeeSerializer(instance=employees , many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST' :
        data=request.data
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(http_method_names=["GET"])
def Employee_detail(request:Request,employee_id:int):
    if request.method == 'GET' :
        employee=Employee.objects.get(pk=employee_id)
        serializer = EmployeeSerializer(instance=employee)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    return Response(data="Employé pas trouvé", status=status.HTTP_404_NOT_FOUND)

