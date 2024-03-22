# Generated by Django 4.2.9 on 2024-03-22 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Enquiry', '0002_rename_intake_interested_month_enquiry_intake_interested_and_more'),
        ('Assessment', '0003_rename_intake_interested_month_assessment_intake_interested_and_more'),
        ('Master', '0008_remove_university_university_status_course_remark'),
    ]

    operations = [
        migrations.DeleteModel(
            name='intake_Year',
        ),
        migrations.AddField(
            model_name='intake',
            name='intake_Name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='intake',
            name='intake_year',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='Duolingo_Exam',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Master.duolingo_exam'),
        ),
        migrations.AlterField(
            model_name='course',
            name='Gmat_Exam',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Master.gmat_exam'),
        ),
        migrations.AlterField(
            model_name='course',
            name='Gre_Exam',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Master.gre_exam'),
        ),
        migrations.AlterField(
            model_name='course',
            name='PTE_Exam',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Master.pte_exam'),
        ),
        migrations.AlterField(
            model_name='course',
            name='Toefl_Exam',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Master.toefl_exam'),
        ),
        migrations.AlterField(
            model_name='course',
            name='bachelor_requirement',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Master.bachelor_requirement'),
        ),
        migrations.AlterField(
            model_name='course',
            name='documents_required',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Master.documents_required'),
        ),
        migrations.AlterField(
            model_name='course',
            name='ielts_Exam',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Master.ielts_exam'),
        ),
        migrations.RemoveField(
            model_name='course',
            name='intake',
        ),
        migrations.AlterField(
            model_name='course',
            name='masters_requirement',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Master.masters_requirement'),
        ),
        migrations.AlterField(
            model_name='course',
            name='tenth_std_percentage_requirement',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Master.tenth_std_percentage_requirement'),
        ),
        migrations.AlterField(
            model_name='course',
            name='twelfth_std_percentage_requirement',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Master.twelfth_std_percentage_requirement'),
        ),
        migrations.AddField(
            model_name='course',
            name='intake',
            field=models.ManyToManyField(blank=True, to='Master.intake'),
        ),
    ]
