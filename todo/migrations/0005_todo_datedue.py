# Generated by Django 4.1.3 on 2023-01-02 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_todo_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='datedue',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
