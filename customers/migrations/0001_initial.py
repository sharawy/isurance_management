# Generated by Django 3.0.7 on 2020-06-22 16:53

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('dob', models.DateField(validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date(2020, 6, 22))])),
            ],
        ),
    ]
