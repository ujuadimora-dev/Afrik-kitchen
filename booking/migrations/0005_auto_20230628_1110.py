# Generated by Django 3.2.19 on 2023-06-28 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20230628_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='table_num',
        ),
        migrations.AddField(
            model_name='table',
            name='category',
            field=models.CharField(choices=[('a', '2'), ('b', '3'), ('c', '4'), ('d', '8'), ('e', '14'), ('f', '20')], default='2', max_length=2),
        ),
        migrations.AddField(
            model_name='table',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='table',
            name='capacity',
            field=models.CharField(choices=[('2', '2_persons'), ('2', '3_persons'), ('4', '4_persons'), ('8', '8_persons'), ('14', '14_persons'), ('20', '20_persons')], default='2_persons', max_length=11),
        ),
        migrations.AlterField(
            model_name='table',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('available', 'Available'), ('not_available', 'Not Available')], default='available', max_length=20),
        ),
        migrations.AlterField(
            model_name='table',
            name='table_position',
            field=models.CharField(choices=[('window', 'Tables by window'), ('middle', 'Tables in middle'), ('outside', 'Tables in the garden'), ('corridor', 'Tables on the corridor')], default='Tables by window', max_length=25),
        ),
    ]
