# Generated by Django 2.1.7 on 2019-03-12 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='quater1_watersupply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Working_place', models.CharField(max_length=50)),
                ('Water_supply_place', models.CharField(max_length=50)),
                ('Electrical_meter_no', models.CharField(max_length=50)),
            ],
        ),
    ]
