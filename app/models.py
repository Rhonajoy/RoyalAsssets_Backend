from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
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


class Characteristics(models.Model):
    
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)

    def __str__(self):
        return f'{self.category}'

class Asset(models.Model):
    type = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category =  models.ForeignKey(Characteristics, on_delete=models.CASCADE, null=True)
    asset_name = models.CharField(max_length=100, null=True)
    asset_value = models.PositiveIntegerField(null=True)


    def __str__(self):
        return f'{self.asset_name}'

URGENCY = (
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low'),

)     

class Request(models.Model):
    type = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    asset_name = models.ForeignKey(Asset, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Characteristics, on_delete=models.CASCADE, null=True)
    urgency = models.CharField(max_length=50, choices=URGENCY, null=True)

    def __str__(self):
        return f'{self.asset_name}-{self.urgency}'   



# from rest_framework import generics, mixins, permissions

# User = get_user_model()

# class UserIsOwnerOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.id == request.user.id

# class UserProfileChangeAPIView(generics.RetrieveAPIView,
#                                mixins.DestroyModelMixin,
#                                mixins.UpdateModelMixin):
#     permission_classes = (
#         permissions.IsAuthenticated,
#         UserIsOwnerOrReadOnly,
#     )
#     serializer_class = UserProfileChangeSerializer
#     #parser_classes = (MultiPartParser, FormParser,)

#     def get_object(self):
#         #username = self.kwargs["username"]
#         username = "moringa"
#         obj = get_object_or_404(User, username=username)
#         return obj

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
