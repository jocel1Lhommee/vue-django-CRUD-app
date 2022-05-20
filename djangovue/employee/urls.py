from django.urls import path
from . import views 

urlpatterns = [
    path('homepage', views.homepage,name="post_home"),
    path('',views.ListEmployee,name="ListEmployee"),
    path('<int:employee_id>',views.Employee_detail,name="Employee_detail")

]