# Generated by Django 2.0.7 on 2018-08-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Itemstock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('quantity', models.IntegerField()),
                ('purchasedate', models.DateField()),
                ('renewaldate', models.DateField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
