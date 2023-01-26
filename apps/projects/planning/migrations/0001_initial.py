# Generated by Django 4.1.4 on 2023-01-26 16:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milestone', models.TextField(max_length=300, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a valid Project name. This value may contain only letters, numbers, and ./-/_/ characters.', regex='^[\\w.-_]+\\Z')])),
                ('task', models.TextField(max_length=300, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a valid Project name. This value may contain only letters, numbers, and ./-/_/ characters.', regex='^[\\w.-_]+\\Z')])),
            ],
        ),
    ]
