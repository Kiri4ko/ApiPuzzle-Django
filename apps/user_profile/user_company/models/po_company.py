from apps.users.models import User
from django.db import models
from apps.auth_reg.validators import (
    validate_company_name, validate_select_industries_name,
)
from apps.common.general_validators import (
    validate_generic_alphanumeric_symbols, validate_generic_latin,
)


# Create model head company.
class POCompany(models.Model):
    #  Company choice
    STARTUP = 'Startup'
    SMALL = 'Small'
    MIDDLE = 'Middle'
    LARGE = 'Large'
    COMPANY = [
        (STARTUP, 'Startup'),
        (SMALL, 'Small (up to 50 people)'),
        (MIDDLE, 'Mid-size (up 200 people)'),
        (LARGE, 'Large (more than 200 people)'),
    ]
    company_name = models.CharField(max_length=255, validators=[validate_company_name], unique=True)
    company_size = models.CharField(max_length=7, choices=COMPANY)
    company_industry = models.CharField(max_length=255, validators=[validate_select_industries_name])
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
    start_project = models.TextField(max_length=25, validators=[validate_generic_latin])
    used_outsourcing = models.CharField(max_length=255, validators=[validate_generic_alphanumeric_symbols])
    employees = models.ManyToManyField(User, related_name='companies_po')

    def __repr__(self):
        return self.company_name

    class Meta:
        ordering = ('company_name',)
        verbose_name = 'PO company'
        verbose_name_plural = 'PO companies'
