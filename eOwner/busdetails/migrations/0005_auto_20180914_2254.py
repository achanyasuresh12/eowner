# Generated by Django 2.0.7 on 2018-09-14 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busdetails', '0004_auto_20180914_2231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='busdetails',
            old_name='mgr_id',
            new_name='mgrid',
        ),
    ]
