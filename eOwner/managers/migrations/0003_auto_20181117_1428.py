# Generated by Django 2.0.7 on 2018-11-17 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0002_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='managers',
            name='mgrage',
        ),
        migrations.RemoveField(
            model_name='managers',
            name='mgrstatus',
        ),
    ]
