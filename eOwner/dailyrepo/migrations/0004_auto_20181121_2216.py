# Generated by Django 2.0.7 on 2018-11-21 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyrepo', '0003_auto_20181121_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyreports',
            name='totalcollection',
            field=models.BigIntegerField(),
        ),
    ]
