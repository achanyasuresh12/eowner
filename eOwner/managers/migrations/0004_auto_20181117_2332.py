# Generated by Django 2.0.7 on 2018-11-17 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0003_auto_20181117_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managers',
            name='mgremail',
            field=models.EmailField(max_length=254),
        ),
    ]
