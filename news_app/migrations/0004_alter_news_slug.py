# Generated by Django 5.1.3 on 2025-01-09 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, unique=True),
        ),
    ]
