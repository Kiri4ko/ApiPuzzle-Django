# Generated by Django 4.1.4 on 2023-01-26 16:14

import apps.auth_reg.validators
import apps.common.general_validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeadCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(message="Only alphanumeric (A-Z, 0-9) and symbols -_:&.' characters are allowed.", regex="^[\\w\\-_:&\\.\\'\\s]*$")])),
                ('logo', models.ImageField(default='logo/company/default/white_background.jpg', max_length=200, null=True, upload_to=apps.auth_reg.validators.change_filename_logo, validators=[apps.common.general_validators.validate_image_extension, apps.auth_reg.validators.validate_image_resolution])),
                ('website', models.URLField(blank=True, null=True)),
                ('tagline', models.CharField(max_length=255)),
                ('industry', models.TextField(max_length=600)),
                ('software_stack', models.TextField(max_length=600)),
                ('select_industries', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Invalid characters, the string should start with letters (A-Z) only and can be used symbols ().', regex='^[a-zA-Z]+[a-zA-Z()\\s]*$')])),
                ('short_description', models.TextField(max_length=600, validators=[django.core.validators.RegexValidator(message='Only alphanumeric (A-Z, 0-9) and symbols characters are allowed.', regex='^[\\w\\W]*$')])),
                ('full_description', models.TextField(max_length=1200, validators=[django.core.validators.RegexValidator(message='Only alphanumeric (A-Z, 0-9) and symbols characters are allowed.', regex='^[\\w\\W]*$')])),
                ('average_hourly_rate', models.DecimalField(decimal_places=2, max_digits=7)),
                ('currency_rate', models.CharField(choices=[('USD', 'Dollars'), ('EUR', 'Euro')], default='USD', max_length=3)),
                ('minimum_project_budget', models.DecimalField(decimal_places=2, max_digits=8)),
                ('currency_budget', models.CharField(choices=[('USD', 'Dollars'), ('EUR', 'Euro')], default='USD', max_length=3)),
                ('team_size', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Minimum = 1'), django.core.validators.MaxValueValidator(999999, message='Maximum = 999 999')])),
                ('location', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Only alphabetic (A-Z) characters are allowed.', regex='^[a-zA-Z\\s]*$')])),
                ('foundation_date', models.DateField(validators=[apps.common.general_validators.validate_no_future_date])),
                ('clients_focus', models.TextField(blank=True, max_length=600, null=True, validators=[django.core.validators.RegexValidator(message='Invalid characters, the string should start with letters (A-Z) only and can be used symbols.', regex='^[a-zA-Z]+[a-zA-Z\\W]*$')])),
                ('contact_marketing', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Only alphanumeric (A-Z, 0-9) and symbols characters are allowed.', regex='^[\\w\\W]*$')])),
                ('contact_expert', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Only alphanumeric (A-Z, 0-9) and symbols characters are allowed.', regex='^[\\w\\W]*$')])),
                ('links_case', models.TextField(max_length=600)),
                ('client_describe', models.TextField(max_length=600)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
                'ordering': ('company_name',),
            },
        ),
    ]
