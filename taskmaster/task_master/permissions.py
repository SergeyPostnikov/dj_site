from rest_framework import permissions 
from django.contrib.auth.models import AnonymousUser


class IsSubscriber(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True


class IsAuthor(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return request.user == obj.user

class IsAnomous:
	def has_object_permission(self, request, view, obj):
		if isinstance(request.user, AnonymousUser):
			return True