# Generated by Django 4.1.4 on 2023-02-02 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_company', '0003_alter_headcompany_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='headcompany',
            old_name='industry',
            new_name='client_industry',
        ),
        migrations.RemoveField(
            model_name='headcompany',
            name='select_industries',
        ),
        migrations.RemoveField(
            model_name='pocompany',
            name='company_industry',
        ),
        migrations.AddField(
            model_name='headcompany',
            name='industry_choice',
            field=models.TextField(choices=[('Ecommerce', 'Ecommerce'), ('AI and Machine Learning', 'AI and Machine Learning'), ('Martech (Marketing Tech)', 'Martech (Marketing Tech)'), ('Live Chat software', 'Live Chat software'), ('Logistics', 'Logistics'), ('Data Science', 'Data Science'), ('HR Software', 'HR Software'), ('Webinar software', 'Webinar software'), ('eLearning', 'eLearning'), ('Cybersecurity', 'Cybersecurity'), ('Augmented Reality', 'Augmented Reality'), ('Project Management software', 'Project Management software'), ('Fintech', 'Fintech'), ('Blockchain', 'Blockchain'), ('Marketplaces', 'Marketplaces'), ('Point of sale software', 'Point of sale software'), ('Mobile Development', 'Mobile Development'), ('Voice recognition', 'Voice recognition'), ('CRM software', 'CRM software'), ('Game Development', 'Game Development'), ('Video (Face) recognition', 'Video (Face) recognition'), ('ERP software', 'ERP software')], default=None, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pocompany',
            name='industry_choice',
            field=models.TextField(choices=[('Ecommerce', 'Ecommerce'), ('AI and Machine Learning', 'AI and Machine Learning'), ('Martech (Marketing Tech)', 'Martech (Marketing Tech)'), ('Live Chat software', 'Live Chat software'), ('Logistics', 'Logistics'), ('Data Science', 'Data Science'), ('HR Software', 'HR Software'), ('Webinar software', 'Webinar software'), ('eLearning', 'eLearning'), ('Cybersecurity', 'Cybersecurity'), ('Augmented Reality', 'Augmented Reality'), ('Project Management software', 'Project Management software'), ('Fintech', 'Fintech'), ('Blockchain', 'Blockchain'), ('Marketplaces', 'Marketplaces'), ('Point of sale software', 'Point of sale software'), ('Mobile Development', 'Mobile Development'), ('Voice recognition', 'Voice recognition'), ('CRM software', 'CRM software'), ('Game Development', 'Game Development'), ('Video (Face) recognition', 'Video (Face) recognition'), ('ERP software', 'ERP software')], default=None, max_length=400),
            preserve_default=False,
        ),
    ]