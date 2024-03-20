# Generated by Django 4.2.9 on 2024-03-20 10:23

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duolingo_Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Overall', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Edu_Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=100)),
                ('Stream', models.CharField(max_length=100)),
                ('Percentage', models.FloatField()),
                ('Year_of_Passing', models.IntegerField()),
                ('Name_of_Institute', models.CharField(max_length=100)),
                ('Medium_of_Education', models.CharField(max_length=100)),
                ('Board', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gmat_Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Verbal', models.FloatField()),
                ('Quantitative', models.FloatField()),
                ('Analytical', models.FloatField()),
                ('overall', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Gre_Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Verbal', models.FloatField()),
                ('Quantitative', models.FloatField()),
                ('Analytical', models.FloatField()),
                ('overall', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ielts_Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Listening', models.FloatField()),
                ('Reading', models.FloatField()),
                ('Writing', models.FloatField()),
                ('Speaking', models.FloatField()),
                ('Overall', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PTE_Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Listening', models.FloatField()),
                ('Reading', models.FloatField()),
                ('Writing', models.FloatField()),
                ('Speaking', models.FloatField()),
                ('Overall', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Rejection_Reason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Refusal_Reason', models.TextField()),
                ('Refusal_Country', django_countries.fields.CountryField(max_length=2)),
                ('Refusal_Visa_Category', models.CharField(max_length=100)),
                ('Refusal_Date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Toefl_Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Listening', models.FloatField()),
                ('Reading', models.FloatField()),
                ('Writing', models.FloatField()),
                ('Speaking', models.FloatField()),
                ('Overall', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Work_Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(max_length=100)),
                ('Designation', models.CharField(max_length=100)),
                ('Start_Date', models.DateField()),
                ('End_Date', models.DateField()),
            ],
        ),
    ]