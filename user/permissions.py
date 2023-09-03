from rest_framework import permissions



class ProfilePermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.user == obj.email:
            return True
        return False