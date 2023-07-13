from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
            return True
        else:
            return bool(request.user and request.user.is_staff)
            # check if the user is admin or not


class IsCreateUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
            return True
        else:
            print("ggg", obj.author)
            print("ggg", request.user.is_staff)
            print("ggg", request)
            return obj.author == request.user or request.user.is_staff
            # check if the user created the review or not
