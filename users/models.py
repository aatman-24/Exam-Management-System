from django.db import models
from django.contrib.auth.models import AbstractUser
from config.roles import ROLES_CHOICES, STUDENT_ROLE

# Create your models here.

class User(AbstractUser):
    role = models.CharField("Role",max_length= 10, choices=ROLES_CHOICES, default=STUDENT_ROLE)