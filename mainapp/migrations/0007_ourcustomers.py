# Generated by Django 3.1.7 on 2021-03-25 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_delete_ourmembers2'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurCustomers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=250)),
                ('customer_surname', models.CharField(max_length=250)),
                ('customer_email', models.URLField(blank=True)),
                ('customer_website', models.CharField(max_length=250)),
                ('customer_phone', models.CharField(max_length=15)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
