# Generated by Django 3.1.7 on 2021-03-26 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_projects_project_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='project_currency',
            field=models.CharField(choices=[('TL', 'Turkish Lira'), ('USD', 'US Dollar'), ('EUR', 'Euro')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='project_price',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
