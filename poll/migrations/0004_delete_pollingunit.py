# Generated by Django 3.2.6 on 2021-08-19 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_pollingunit'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PollingUnit',
        ),
    ]
