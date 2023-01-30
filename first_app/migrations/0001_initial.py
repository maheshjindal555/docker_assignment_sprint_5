# Generated by Django 4.1.3 on 2022-12-05 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=30)),
                ('emp_address', models.CharField(max_length=30)),
                ('emp_id', models.IntegerField()),
            ],
        ),
    ]
