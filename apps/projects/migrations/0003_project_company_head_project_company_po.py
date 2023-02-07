# Generated by Django 4.1.4 on 2023-02-06 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_company', '0012_alter_headcompany_owner'),
        ('projects', '0002_alter_project_project_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='company_head',
            field=models.ForeignKey(default=None, on_delete=models.SET('company removed'), related_name='project_head', to='user_company.headcompany'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='company_po',
            field=models.ForeignKey(default=None, on_delete=models.SET('company removed'), related_name='project_po', to='user_company.headcompany'),
            preserve_default=False,
        ),
    ]