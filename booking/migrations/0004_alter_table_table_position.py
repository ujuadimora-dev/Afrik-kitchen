# Generated by Django 3.2.19 on 2023-06-30 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20230630_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='table_position',
            field=models.CharField(choices=[('  by window', 'by window'), ('  in middle of the room', ' in middle'), ('  in Resturant garden', 'in Resturant garden'), ('  on the corridor', ' on the corridor')], default='Tables by window', max_length=25),
        ),
    ]
