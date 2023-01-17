from django.db import models

from ..validators import validate_project_name


class Planning(models.Model):
    milestone = models.TextField(max_length=300, validators=[validate_project_name], unique=True)
    task = models.TextField(max_length=300, validators=[validate_project_name], unique=True)
