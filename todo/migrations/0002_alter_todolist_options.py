# Generated by Django 4.1.4 on 2023-01-13 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ('-slug',)},
        ),
    ]
