# Generated by Django 4.0.4 on 2022-05-23 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_delete_task_alter_diseases_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='symptoms',
            name='therapy',
        ),
    ]
