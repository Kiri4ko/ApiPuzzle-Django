from django.db import models
from ..user_profile.user_company.models.head_company import HeadCompany
from ..users.models import User


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    company_head = models.ForeignKey(
        HeadCompany, on_delete=models.SET_NULL, related_name='project_head', null=True
    )
    company_po = models.ForeignKey(
        HeadCompany, on_delete=models.SET_NULL, related_name='project_po', null=True
    )
    user = models.ManyToManyField(User, related_name='project')

    def __repr__(self):
        return self.project_name

    class Meta:
        ordering = ('project_name',)
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
