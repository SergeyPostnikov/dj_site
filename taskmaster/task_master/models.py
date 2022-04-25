from django.db import models
from django.contrib.auth.models import User, AbstractUser



class CustomUser(AbstractUser):
	REQUIRED_FIELDS = ['email', 'password']
	ROLES = (
		('a', 'author'),
		('s', 'subscriber')
		)
	email = models.EmailField()
	role = models.CharField('Роль', max_length=1, choices=ROLES, default='s')



class PubSub(models.Model):
	pubs = models.ManyToManyField(CustomUser, verbose_name='Авторы')


class Todo(models.Model):
	content = models.TextField(blank=False, verbose_name="I want to ")
	created_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(CustomUser, verbose_name='Автор', on_delete=models.PROTECT)
	private = models.BooleanField(default=True, verbose_name='Только для подписчиков')


	def __str__(self):
		return self.content

