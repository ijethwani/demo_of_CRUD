from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Employee
from .serializers import Employee_Serializer

class EmployeeCreateView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employee_Serializer

class EmployeeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employee_Serializer
    lookup_field = "pk"
