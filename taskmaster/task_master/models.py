from django.db import models
from django.contrib.auth.models import User




class Todo(models.Model):
	content = models.TextField(blank=False, verbose_name="I want to ")
	created_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.PROTECT)
	private = models.BooleanField(default=True, verbose_name='Только для подписчиков')


	def __str__(self):
		return self.content


# class Subscribers(models.Model):
# 	author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE) 
# 	user = models.ForeignKey(User, verbose_name='Подписчик', on_delete=models.CASCADE)
