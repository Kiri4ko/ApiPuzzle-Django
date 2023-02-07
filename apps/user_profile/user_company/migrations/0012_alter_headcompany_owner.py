# Generated by Django 4.1.4 on 2023-02-06 10:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_company', '0011_alter_headcompany_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headcompany',
            name='owner',
            field=models.OneToOneField(on_delete=models.SET('owner removed'), related_name='company_head', to=settings.AUTH_USER_MODEL),
        ),
    ]
