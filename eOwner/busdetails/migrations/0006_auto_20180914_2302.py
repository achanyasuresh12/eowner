# Generated by Django 2.0.7 on 2018-09-14 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busdetails', '0005_auto_20180914_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='busdetails',
            old_name='mgrid',
            new_name='mgr_id',
        ),
    ]