from django.db import models


class Project(models.Model):
    project_name = models.TextField(max_length=300, unique=True)
