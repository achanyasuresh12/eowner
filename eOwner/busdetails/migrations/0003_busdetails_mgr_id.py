# Generated by Django 2.0.7 on 2018-09-14 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busdetails', '0002_busdetails_seatorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='busdetails',
            name='mgr_id',
            field=models.BigIntegerField(default=12),
            preserve_default=False,
        ),
    ]