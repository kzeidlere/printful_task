# Generated by Django 3.2.4 on 2021-06-04 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='check',
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='date',
        ),
        migrations.AddField(
            model_name='todolist',
            name='apraksts',
            field=models.TextField(default='apraksts'),
        ),
        migrations.AddField(
            model_name='todolist',
            name='virsraksts',
            field=models.CharField(default='virsraksts', max_length=20),
        ),
    ]
