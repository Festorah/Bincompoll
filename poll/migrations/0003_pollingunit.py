# Generated by Django 3.2.6 on 2021-08-19 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('poll', '0002_delete_pollingunit'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollingUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.IntegerField()),
                ('polling_unit_id', models.IntegerField()),
                ('ward_id', models.IntegerField()),
                ('lga_id', models.IntegerField()),
                ('unique_ward_id', models.IntegerField()),
                ('polling_unit_number', models.IntegerField()),
                ('polling_unit_name', models.CharField(max_length=200)),
                ('polling_unit_description', models.TextField(blank=True, default='Polling unit description...', null=True)),
            ],
        ),
    ]
