# Generated by Django 4.2 on 2024-03-26 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sop', models.FileField(blank=True, null=True, upload_to='sop')),
                ('cv', models.FileField(blank=True, null=True, upload_to='cv')),
                ('passport', models.FileField(blank=True, null=True, upload_to='passport')),
                ('ielts', models.FileField(blank=True, null=True, upload_to='ielts')),
                ('gre', models.FileField(blank=True, null=True, upload_to='gre')),
                ('toefl', models.FileField(blank=True, null=True, upload_to='toefl')),
                ('gmat', models.FileField(blank=True, null=True, upload_to='gmat')),
                ('pte', models.FileField(blank=True, null=True, upload_to='pte')),
                ('work_experience', models.FileField(blank=True, null=True, upload_to='work_experience')),
                ('diploma_marksheet', models.FileField(blank=True, null=True, upload_to='diploma_marksheet')),
                ('bachelor_marksheet', models.FileField(blank=True, null=True, upload_to='bachelor_marksheet')),
                ('master_marksheet', models.FileField(blank=True, null=True, upload_to='master_marksheet')),
                ('other_documents', models.FileField(blank=True, null=True, upload_to='other_documents')),
            ],
        ),
    ]
