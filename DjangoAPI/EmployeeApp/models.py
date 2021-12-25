from django.db import models

# Create your models here.
class Departments(models.Model):
    """
    Model representing a department
    """
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=50)

class Employees(models.Model):
    """
    Model representing an employee
    """
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=50)
    Department = models.CharField(max_length=50)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=50)