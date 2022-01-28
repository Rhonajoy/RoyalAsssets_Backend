from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class User(AbstractUser):
    

    class Types(models.TextChoices):
        #users
        ADMINISTRATOR = "ADMINISTRATOR", "Administrator"
        PROC_MANAGER = "PROC_MANAGER", "Proc_Manager"
        EMPLOYEE = "EMPLOYEE", "Employee"

    base_type = Types.EMPLOYEE

    type = models.CharField(
        _("Types"), max_length=50, choices=Types.choices, default= base_type
    )

    name = models.CharField(
        _("Name of User"), blank=True, max_length=255
    )

    def get_absolute_url(self):
        return reverse ("users:detail", kwargs={"username": self.username})


    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)


    """"proxy model managers"""       

class AdministratorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.ADMINISTRATOR) 

class Proc_ManagerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.PROC_MANAGER)  

class EmployeeManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.EMPLOYEE)        


class AdministratorMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    """proxy models"""  
class Administrator(User):
    base_type = User.Types.ADMINISTRATOR
    objects = AdministratorManager()

    class Meta:
        proxy = True

    def delete(self):
        return "delete"


class Proc_ManagerMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=255)
        

class Proc_Manager(User):
    base_type = User.Types.PROC_MANAGER
    objects = Proc_ManagerManager()

    @property
    def more(self):
        return self.proc_managermore

    class Meta:
        proxy = True 

    def approve(self):
        return "Go ahead"   

class EmployeeMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    section = models.CharField(max_length=255)
               

class Employee(User):
    base_type = User.Types.EMPLOYEE
    objects = EmployeeManager()

    @property
    def more(self):
        return self.employeemore

    class Meta:
        proxy = True      

    def request(self):
        return "request"
