# Generated by Django 3.2.19 on 2023-06-16 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view_menu', '0006_alter_breakfast_fimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakfast',
            name='fimage',
            field=models.URLField(),
        ),
    ]
