from apps.users.models import User
from django.db import models
from apps.auth_reg.validators import validate_company_name, validate_list_industry
from apps.common.general_validators import (
    validate_generic_alphanumeric_symbols
)

from .choices import CompanyChoice, ProjectStart


# Create model head company.
class POCompany(models.Model):
    company_name = models.CharField(max_length=255, validators=[validate_company_name], unique=True)
    company_size = models.CharField(max_length=7, choices=CompanyChoice.COMPANY)
    industry_choice = models.TextField(max_length=400, validators=[validate_list_industry])
    dev_team = models.CharField(
        max_length=255, validators=[validate_generic_alphanumeric_symbols], name='development_team'
    )
    outsourcing = models.CharField(
        max_length=255, validators=[validate_generic_alphanumeric_symbols], name='use_outsourcing'
    )
    desc_project = models.TextField(
        max_length=600, validators=[validate_generic_alphanumeric_symbols], name='description_project'
    )

    business_req = models.CharField(
        max_length=255, validators=[validate_generic_alphanumeric_symbols], name='business_requirements'
    )
    tech_stack = models.CharField(
        max_length=255, validators=[validate_generic_alphanumeric_symbols], name='technological_stack'
    )
    link_competitor = models.TextField(max_length=255)
    start_project = models.CharField(max_length=19, choices=ProjectStart.TIMESTART)
    used_outsourcing = models.CharField(max_length=255, validators=[validate_generic_alphanumeric_symbols])
    owner = models.OneToOneField(User, on_delete=models.SET('owner removed'), related_name='company_po')
    is_active = models.BooleanField(default=False)  # Activation status company

    def __repr__(self):
        return self.company_name

    class Meta:
        ordering = ('company_name',)
        verbose_name = 'PO company'
        verbose_name_plural = 'PO companies'
