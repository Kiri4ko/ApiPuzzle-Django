# Generated by Django 4.1.4 on 2023-01-26 16:14

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('full_name', models.CharField(max_length=160, validators=[django.core.validators.RegexValidator(message='Only alphabetic (A-Z) characters are allowed.', regex='^[a-zA-Z\\s]*$')])),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('CEO', 'CEO'), ('CTO', 'CTO'), ('Designer', 'Designer'), ('Product Owner', 'Product Owner'), ('Programmer', 'Programmer'), ('Project Manager', 'Project Manager'), ('QA', 'QA')], max_length=15, validators=[django.core.validators.MinLengthValidator(2)])),
                ('is_staff', models.BooleanField(default=False)),
                ('registered', models.DateTimeField(auto_now_add=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=16, region=None, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ('email',),
            },
        ),
    ]