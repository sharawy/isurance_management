# Generated by Django 3.0.7 on 2020-06-22 17:26

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='dob',
            field=models.DateField(help_text='Enter the date of birth', validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date(2020, 6, 22))], verbose_name='Date of birth'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=256, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=256, verbose_name='Last name'),
        ),
    ]
