# Generated by Django 2.0.7 on 2018-11-11 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0002_remove_purchases_mgr_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchases',
            name='mgr_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]