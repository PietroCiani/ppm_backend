# Generated by Django 4.2.2 on 2023-06-11 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_todo_options_todo_due_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={},
        ),
        migrations.RemoveField(
            model_name='todo',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
    ]
