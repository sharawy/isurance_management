# Generated by Django 3.0.7 on 2020-06-22 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('personal-accident', 'Personal Accident'), ('travel', 'Borrowed by someone'), ('property', 'Archived - not available anymore')], max_length=25)),
                ('premium', models.DecimalField(decimal_places=2, max_digits=12)),
                ('cover', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]
