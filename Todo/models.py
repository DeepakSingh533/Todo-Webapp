from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class todo(models.Model):
	text = models.CharField(max_length=40)
	complete = models.BooleanField(default=False)
	user_name = models.CharField(max_length=50)

	def __str__(self):
		return self.user_name	


	
