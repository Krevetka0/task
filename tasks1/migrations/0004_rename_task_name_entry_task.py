# Generated by Django 5.0.2 on 2024-02-07 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks1', '0003_rename_task_todolist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='task_name',
            new_name='task',
        ),
    ]