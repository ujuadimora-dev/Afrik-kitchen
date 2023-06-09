# Generated by Django 3.2.19 on 2023-06-15 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view_menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuprice',
            name='Pimage',
        ),
        migrations.AddField(
            model_name='menuprice',
            name='fimage',
            field=models.ImageField(default="'default.jpg'", upload_to='menu_images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menuprice',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='menuprice',
            name='priceL',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='menuprice',
            name='priceM',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
