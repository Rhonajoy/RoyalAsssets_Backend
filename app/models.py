from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


# Create your models here.
class Role(models.Model):
    """This defines the new roles a user can have

    Args:
        models ([type]): [description]

    Raises:
        ValueError: [description]
        ValueError: [description]

    Returns:
        [type]: [description]
    """

    name = models.CharField(
        max_length=30, verbose_name="The role of a user in the organisation"
    )

    def insert_roles(self):
        roles = ["ADMINISTRATOR", "PROCUREMENT_MANAGER", "EMPLOYEE"]
        for role in roles:
            new_role = Role(name=role)
            new_role.save()

    def __str__(self):
        return self.name


class User(AbstractUser):
    # roles
    ADMINISTRATOR = 1
    PROCUREMENT_MANAGER = 2
    EMPLOYEE = 3
    # roles choices
    ROLES = (
        (ADMINISTRATOR, "Administrator"),
        (PROCUREMENT_MANAGER, "Procurement Manager"),
        (EMPLOYEE, "Employee"),
    )

    # user roles
    role = models.PositiveSmallIntegerField(choices=ROLES,null=True)

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

ROLES = (
    ('Admin', 'Admin'),
    ('Procurement_Manager', 'Procurement_Manager'),
    ('Employee', 'Employee'),
)
class Profile(models.Model):
    full_name=models.CharField(max_length=50, blank=True, null=True)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    email=models.EmailField(max_length = 200)
    role=models.CharField(max_length=50, choices=ROLES, null=True)
    profile_photo = CloudinaryField('image')
    contact = models.CharField(max_length=50, blank=True, null=True)
    

    def update(self):
        self.save()

    def save_profile(self):
        self.save()
    def __str__(self):
        return self.full_name

    def delete_profile(self):
        self.delete()
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Furniture', 'Furniture'),
)        

class Asset(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY)
    asset_value = models.PositiveIntegerField()
    quantity=models.IntegerField()
    


    def __str__(self):
        return f'{self.name}'

URGENCY = (
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low'),

)     
TYPE = (
    ('Request', 'Request'),
    ('Repair', 'Repair'),
   
)  
STATUS=(
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Declined', 'Declined'),
    
)      
class RequestAsset(models.Model):
    type = models.CharField(max_length=50, choices=TYPE, null=True)
    asset_name = models.CharField(max_length=50,null=True)
    quantity=models.IntegerField()
    urgency = models.CharField(max_length=50, choices=URGENCY, null=True)
    is_approved=models.CharField(max_length=50, choices=STATUS,default='Pending', null=True)
    employee_name = models.ForeignKey(User, max_length=50,on_delete=models.CASCADE,null=True)



    def __str__(self):
        return f'{self.asset_name}-{self.urgency}'   



DEPARTMENT = (
    ('Finance', 'Finance'),
    ('Human Resource', 'Human Resource'),
    ('Marketing', 'Marketing')
)

class Add_staff(models.Model):
    contact = models.IntegerField(User, null=True)
    username = models.CharField(User, max_length=15, null=True)
    # username = models.ForeignKey(User, max_length=50,on_delete=models.CASCADE,null=True)
    #role = models.CharField(max_length=50, choices=ROLES, null=True)
    #employee_name = models.ForeignKey(User, max_length=50,on_delete=models.CASCADE,null=True)
    department = models.CharField(User, max_length=15, choices=DEPARTMENT , null=True)

    def update(self):
        self.save()

    def save_add_staff(self):
        self.save()

    def delete_add_staff(self):
        self.delete()

    
    def __str__(self):
        return f'{self.username}'



