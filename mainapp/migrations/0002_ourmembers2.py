# Generated by Django 3.1.7 on 2021-03-23 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurMembers2',
            fields=[
                ('member', models.ForeignKey(help_text='Please select from the list', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('expertise', models.CharField(choices=[('Frontend Developer', 'Frontend Developer'), ('Backend Developer', 'Backend Developer'), ('Full Stack Developer', 'Full Stack Developer')], max_length=100)),
            ],
        ),
    ]
