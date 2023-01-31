from apps.users.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.auth_reg.validators import (
    validate_company_name, validate_select_industries_name,
    validate_image_resolution, change_filename_logo,
)
from apps.common.general_validators import (
    validate_generic_alphanumeric_symbols, validate_no_future_date,
    validate_generic_latin_symbols, validate_generic_latin,
    validate_image_extension,
)


# Create model head company.
class HeadCompany(models.Model):
    #  Currency selection
    USD = 'USD'
    EUR = 'EUR'
    CURRENCIES = [
        (USD, 'Dollars'),
        (EUR, 'Euro'),
    ]
    company_name = models.CharField(max_length=255, validators=[validate_company_name], unique=True)
    logo = models.ImageField(
        upload_to=change_filename_logo, max_length=200,
        default='logo/company/default/white_background.jpg',
        validators=[validate_image_extension, validate_image_resolution], null=True
    )
    website = models.URLField(max_length=200, blank=True, null=True)
    tagline = models.CharField(max_length=255)
    industry = models.TextField(max_length=600)
    software_stack = models.TextField(max_length=600)
    select_industries = models.CharField(max_length=255, validators=[validate_select_industries_name])
    desc_s = models.TextField(max_length=600, validators=[validate_generic_alphanumeric_symbols],
                              name='short_description')
    desc_f = models.TextField(max_length=1200, validators=[validate_generic_alphanumeric_symbols],
                              name='full_description')
    rate = models.DecimalField(max_digits=7, decimal_places=2, name='average_hourly_rate')
    currency_rate = models.CharField(max_length=3, choices=CURRENCIES, default=USD)
    min_budget = models.DecimalField(max_digits=8, decimal_places=2, name='minimum_project_budget')
    currency_budget = models.CharField(max_length=3, choices=CURRENCIES, default=USD)
    team_size = models.IntegerField(
        validators=[
            MinValueValidator(1, message='Minimum = 1'),
            MaxValueValidator(999999, message='Maximum = 999 999')
        ]
    )
    location = models.CharField(max_length=255, validators=[validate_generic_latin])
    foundation_date = models.DateField(validators=[validate_no_future_date])
    clients_focus = models.TextField(max_length=600, blank=True, null=True, validators=[validate_generic_latin_symbols])
    contact_marketing = models.CharField(max_length=255, validators=[validate_generic_alphanumeric_symbols])
    contact_expert = models.CharField(max_length=255, validators=[validate_generic_alphanumeric_symbols])
    links_case = models.TextField(max_length=600)
    client_desc = models.TextField(max_length=600, name='client_describe')
    employees = models.ManyToManyField(User, related_name='companies_head')

    def __repr__(self):
        return self.company_name

    class Meta:
        ordering = ('company_name',)
        verbose_name = 'Head company'
        verbose_name_plural = 'Head companies'
