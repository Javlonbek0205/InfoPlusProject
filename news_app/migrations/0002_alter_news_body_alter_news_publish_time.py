# Generated by Django 5.1.3 on 2024-11-28 14:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
