# Generated by Django 4.1.4 on 2023-02-07 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('project_name',), 'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
    ]
