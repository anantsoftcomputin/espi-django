# Generated by Django 4.2.9 on 2024-03-22 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0002_duolingo_exam_edu_level_gmat_exam_gre_exam_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='application_form',
            field=models.FileField(blank=True, upload_to='application_forms/', verbose_name='Application Form'),
        ),
        migrations.AddField(
            model_name='university',
            name='bachelor_requirement',
            field=models.CharField(blank=True, max_length=255, verbose_name='Bachelor Degree Requirement'),
        ),
        migrations.AddField(
            model_name='university',
            name='duolingo_requirement',
            field=models.CharField(blank=True, max_length=255, verbose_name='Duolingo Requirement'),
        ),
        migrations.AddField(
            model_name='university',
            name='gmat_requirement',
            field=models.CharField(blank=True, max_length=255, verbose_name='GMAT Requirement'),
        ),
        migrations.AddField(
            model_name='university',
            name='gre_requirement',
            field=models.CharField(blank=True, max_length=255, verbose_name='GRE Requirement'),
        ),
        migrations.AddField(
            model_name='university',
            name='ielts_requirement',
            field=models.CharField(blank=True, max_length=255, verbose_name='IELTS Requirement'),
        ),
        migrations.AddField(
            model_name='university',
            name='masters_requirement',
            field=models.CharField(blank=True, max_length=255, verbose_name='Masters Degree Requirement'),
        ),
        migrations.AddField(
            model_name='university',
            name='newsletter',
            field=models.BooleanField(default=False, verbose_name='Newsletter Subscription'),
        ),
        migrations.AddField(
            model_name='university',
            name='pte_requirement',
            field=models.CharField(blank=True, max_length=255, verbose_name='PTE Requirement'),
        ),
        migrations.AddField(
            model_name='university',
            name='tenth_std_percentage_requirement',
            field=models.FloatField(default=10, verbose_name='10th Std % Requirement'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='toefl_requirement',
            field=models.CharField(blank=True, max_length=255, verbose_name='TOEFL Requirement'),
        ),
        migrations.AddField(
            model_name='university',
            name='twelfth_std_percentage_requirement',
            field=models.FloatField(default=10, verbose_name='12th Std % Requirement'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='university_status',
            field=models.BooleanField(default=True, verbose_name='University Active Status'),
        ),
    ]
