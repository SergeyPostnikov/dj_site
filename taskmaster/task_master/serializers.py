from rest_framework import serializers
from .models import Todo, CustomUser
 

class TodoSerializer(serializers.ModelSerializer):
	
	# user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = Todo
		fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = CustomUser
		# fields = ('id', "email", "password")
		fields = '__all__'
		