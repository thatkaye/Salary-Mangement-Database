# Generated by Django 3.2.7 on 2021-10-06 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salarymanagement', '0014_auto_20210929_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='year_hired',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]