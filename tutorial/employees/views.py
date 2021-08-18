import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializers, EmployeeCreateSerializer


# Create your views here.

class EmployeeViews(APIView):

    def get(self, request, pk=None, *args, **kwargs):
        employee_id = pk

        if employee_id is not None:
            queryset = Employee.objects.get(employee_id=employee_id)
            data = EmployeeSerializers(queryset, many=False)
            return Response(data=data.data, status=status.HTTP_200_OK)

        queryset = Employee.objects.all()
        data = EmployeeSerializers(queryset, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        data = EmployeeCreateSerializer(data=request.data)

        if data.is_valid():
            data.save()
            return Response(data=data.data, status=status.HTTP_201_CREATED)

        return Response(data=data.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, *args, **kwargs):

        employee_id = pk
        emp = Employee.objects.get(employee_id=employee_id)
        data = EmployeeCreateSerializer(emp, data=request.data)

        if data.is_valid():
            data.save()
            return Response(data=data.data, status=status.HTTP_200_OK)

        return Response(data=data.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, *args, **kwargs):

        employee_id = pk
        emp = Employee.objects.get(employee_id=employee_id)
        data = EmployeeCreateSerializer(emp, data=request.data, partial=True)

        if data.is_valid():
            data.save()
            return Response(data=data.data, status=status.HTTP_200_OK)

        return Response(data=data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, *args, **kwargs):

        employee_id = pk
        emp = Employee.objects.get(employee_id=employee_id)
        emp.delete()
        return Response(data={"message": "Data Deleted"}, status=status.HTTP_400_BAD_REQUEST)