# Generated by Django 2.0.7 on 2018-11-20 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0005_auto_20181117_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managers',
            name='mgremail',
            field=models.EmailField(max_length=254),
        ),
    ]
