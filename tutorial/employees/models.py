from datetime import datetime

from django.db import models


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100, blank=False, null=True)

    class Meta:
        db_table = 'department'

    def __str__(self):
        return self.department_name


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100, blank=False, null=True)
    employee_email = models.CharField(max_length=100, blank=False, null=True)
    employee_department = models.ForeignKey(Department,
                                            on_delete=models.DO_NOTHING,
                                            db_column='department_id',
                                            blank=True,
                                            null=True
                                            )
    created_date = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.employee_name
