# Generated by Django 4.2.9 on 2024-03-27 06:08

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Enquiry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='student_country',
            field=django_countries.fields.CountryField(default='IN', max_length=2),
        ),
    ]