from rest_framework import serializers
from .models import Employee, Department


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        depth = 1


class EmployeeCreateSerializer(serializers.ModelSerializer):

    employee_name = serializers.CharField(max_length=100)
    employee_email = serializers.EmailField(max_length=100)
    employee_department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())

    class Meta:
        model = Employee
        fields = '__all__'

    def validate_employee_email(self, data):
        if not data.lower().endswith("@bioclinica.com"):
            raise serializers.ValidationError("You are not an Bioclinica employee")
        return data
