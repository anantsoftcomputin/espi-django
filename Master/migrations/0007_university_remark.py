# Generated by Django 4.2.9 on 2024-03-22 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0006_bachelor_requirement_masters_requirement_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='Remark',
            field=models.TextField(blank=True, verbose_name='Notes'),
        ),
    ]
