# Generated by Django 2.0.7 on 2018-11-21 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busdetails', '0012_auto_20181117_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busdetails',
            name='arrival_time',
            field=models.TimeField(),
        ),
    ]