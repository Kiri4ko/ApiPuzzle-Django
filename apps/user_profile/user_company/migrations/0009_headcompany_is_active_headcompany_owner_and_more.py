# Generated by Django 4.1.4 on 2023-02-06 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_company', '0008_remove_pocompany_employees_pocompany_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='headcompany',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='headcompany',
            name='owner',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='owner_company', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pocompany',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='headcompany',
            name='employees',
        ),
        migrations.AlterField(
            model_name='pocompany',
            name='owner',
            field=models.OneToOneField(on_delete=models.SET('owner removed'), related_name='company_po', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='headcompany',
            name='employees',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='companies_head', to=settings.AUTH_USER_MODEL),
        ),
    ]