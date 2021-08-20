# Generated by Django 3.2.6 on 2021-08-19 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('poll', '0004_delete_pollingunit'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollingUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.IntegerField(verbose_name='unique_id')),
                ('polling_unit_id', models.IntegerField(verbose_name='polling_unit_id')),
                ('ward_id', models.IntegerField(verbose_name='ward_id')),
                ('lga_id', models.IntegerField(verbose_name='lga_id')),
                ('unique_ward_id', models.IntegerField(verbose_name='unique_ward_id')),
                ('polling_unit_number', models.CharField(max_length=200, verbose_name='polling_unit_number')),
                ('polling_unit_name', models.CharField(max_length=200, verbose_name='polling_unit_name')),
                ('polling_unit_description', models.TextField(blank=True, default='Polling unit description...', null=True, verbose_name='polling_unit_description')),
            ],
        ),
    ]
