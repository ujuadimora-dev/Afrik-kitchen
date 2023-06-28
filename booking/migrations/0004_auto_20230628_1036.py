# Generated by Django 3.2.19 on 2023-06-28 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_table_table_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='capacity',
            field=models.IntegerField(choices=[('2', '2_persons'), ('2', '3_persons'), ('4', '4_persons'), ('8', '8_persons'), ('14', '14_persons'), ('20', '20_persons')], default=2),
        ),
        migrations.AlterField(
            model_name='table',
            name='table_num',
            field=models.IntegerField(choices=[('a', '2'), ('b', '3'), ('c', '4'), ('d', '8'), ('e', '14'), ('f', '20')], null=True),
        ),
    ]