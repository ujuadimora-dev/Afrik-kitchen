# Generated by Django 3.2.19 on 2023-06-23 00:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_previous_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='creat_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
