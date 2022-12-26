# TODO здесь производится настройка пермишенов для нашего проекта
from rest_framework.permissions import BasePermission

from users.models import UserRoles


class Is_not_Admin(BasePermission):
    def has_permission(self, request, view):
        rez = request.user and request.user.is_authenticated
        return rez

    def has_object_permission(self, request, view, object):
        rez = request.user and request.user and object.author == request.user
        return rez


class Is_Admin(BasePermission):
    def has_permission(self, request, view):
        rez = request.user and request.user.is_authenticated
        return rez

    def has_object_permission(self, request, view, object):
        rez = request.user.role == UserRoles.ADMIN
        return rez
