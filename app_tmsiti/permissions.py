from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrPostOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        elif request.method in SAFE_METHODS:
            return request.user and (
                        request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser))
        return request.user and request.user.is_authenticated and request.user.is_staff
