# Generated by Django 4.2.5 on 2023-09-23 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_subject_student_link_stu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='dept_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]