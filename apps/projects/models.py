from django.db import models

from .planning.models import Planning

from ..users.models import User


class Project(models.Model):
    project_name = models.TextField(max_length=300, unique=True)
    planning = models.ForeignKey(Planning, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
