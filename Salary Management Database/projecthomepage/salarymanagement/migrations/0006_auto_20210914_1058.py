# Generated by Django 3.2.6 on 2021-09-14 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salarymanagement', '0005_alter_salary_employee_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary',
            name='employee_id',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Salary',
        ),
    ]