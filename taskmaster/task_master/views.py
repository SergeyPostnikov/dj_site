from django.shortcuts import render
from rest_framework import generics, viewsets
from django.contrib.auth.models import User

from django.contrib.auth.models import AnonymousUser

from .permissions import *

from .serializers import TodoSerializer, UserSerializer

from .models import Todo, CustomUser
# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer
	# permission_classes = (IsSubscriber, IsAuthor)
	permission_classes = (IsAuthor, )
	def list(self, request):
		if isinstance(request.user, AnonymousUser):
			self.queryset = Todo.objects.filter(private=False)
		# elif request.user
		return super().list(self, request)

			

class UserViewSet(viewsets.ModelViewSet):
	queryset = CustomUser.objects.all()
	serializer_class = UserSerializer


