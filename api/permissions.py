from rest_framework import permissions


class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
            return True
        else:
            return bool(request.user and request.user.is_staff)
            # check if the user is admin or not


class ReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
            return True
        else:
            return obj.review_user == request.user
            # check if the user created the review or not
