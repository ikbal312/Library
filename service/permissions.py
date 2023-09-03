from rest_framework import permissions

class NotificationPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        print(vars(view))
        if request.user.is_authenticated:
            return True
        return False

        
class ReservationPermisssion(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

        
class ReminderPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

        
class BorrowPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    

class WishlistPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if str(request.user) == str(obj.user_id):

            return True
        return False