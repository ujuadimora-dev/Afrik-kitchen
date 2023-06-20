# Generated by Django 3.2.19 on 2023-06-20 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view_menu', '0009_auto_20230617_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='breakfast',
            name='calorie_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='breakfast',
            name='created_by_staff',
            field=models.CharField(default='Unknown', max_length=25),
        ),
        migrations.AddField(
            model_name='breakfast',
            name='created_on',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='breakfast',
            name='vegetarian',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dinner',
            name='calorie_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dinner',
            name='created_by_staff',
            field=models.CharField(default='Unknown', max_length=25),
        ),
        migrations.AddField(
            model_name='dinner',
            name='created_on',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='dinner',
            name='description',
            field=models.TextField(default='Unknown', max_length=25),
        ),
        migrations.AddField(
            model_name='dinner',
            name='vegetarian',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lunch',
            name='calorie_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lunch',
            name='created_by_staff',
            field=models.CharField(default='Unknown', max_length=25),
        ),
        migrations.AddField(
            model_name='lunch',
            name='created_on',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='lunch',
            name='description',
            field=models.TextField(default='Unknown', max_length=25),
        ),
        migrations.AddField(
            model_name='lunch',
            name='vegetarian',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sides',
            name='calorie_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sides',
            name='created_by_staff',
            field=models.CharField(default='Unknown', max_length=25),
        ),
        migrations.AddField(
            model_name='sides',
            name='created_on',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='sides',
            name='description',
            field=models.TextField(default='Unknown', max_length=25),
        ),
        migrations.AddField(
            model_name='sides',
            name='vegetarian',
            field=models.BooleanField(default=False),
        ),
    ]