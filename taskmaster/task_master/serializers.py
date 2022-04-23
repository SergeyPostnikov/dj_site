from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer):
	
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = Todo
		# fields = ('content', 'user')
		fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', "email")