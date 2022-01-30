from rest_framework import permissions
from django.contrib.auth.models import Group


class CreateUserPermission(permissions.BasePermission):
    """This determines whether a user is authorized to create users depending on their group

    Args:
        permissions ([type]): [description]
    """

    def has_permission(self, request, view):
        if (
            request.user.role.name == "ADMINISTRATOR"
            or request.user.role.name == "PROCUREMENT_MANAGER"
            # or request.user.role.name == "EMPLOYEE"
        ):
            return True
        else:
            return False


class DeleteUserPermission(permissions.BasePermission):
    """This determines whether a user is authorized to create users depending on their group

    Args:
        permissions ([type]): [description]
    """

    def has_permission(self, request, view):
        if (
            request.user.role.name == "ADMINISTRATOR"
            or request.user.role.name == "PROCUREMENT_MANAGER"
        ):
            return True
        else:
            return False
