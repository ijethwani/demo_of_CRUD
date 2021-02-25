
from django.urls import path
from .views import EmployeeCreateView,EmployeeDetailView

urlpatterns = [
    path("",EmployeeCreateView.as_view(),name="home"),
    path("detail/<pk>",EmployeeDetailView.as_view(),name="detail")
]