from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

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
    role = models.PositiveSmallIntegerField(choices=ROLES, default=EMPLOYEE)

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)