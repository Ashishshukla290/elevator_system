# Generated by Django 4.1.4 on 2023-11-18 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0002_elevator_requests_alter_elevator_current_floor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elevator',
            name='direction',
            field=models.CharField(default='still', max_length=20),
        ),
    ]
