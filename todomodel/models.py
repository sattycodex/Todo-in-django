from django.db import models
from django.contrib.auth.models import User,auth

# Create your models here.

class todo(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    todo_name=models.CharField( max_length=200)
    is_complete=models.BooleanField(default=False)

    def __str__(self):
        return self.todo_name
