# Generated by Django 2.0.7 on 2018-09-19 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketbooking',
            name='user_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
