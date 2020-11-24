from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LupaPassword(models.Model):
    token = models.CharField(max_length=16)
    is_used = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)