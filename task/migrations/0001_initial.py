# Generated by Django 4.2.2 on 2023-06-09 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('created_by', models.CharField(default='Anonymous', max_length=150)),
                ('assigned_to', models.CharField(default='Anonymous', max_length=150)),
                ('due_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
