# Generated by Django 4.1.4 on 2023-03-01 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_travel_agency_mobile_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel_agency',
            name='mobile_no',
            field=models.CharField(default=None, max_length=10, unique=True),
        ),
    ]