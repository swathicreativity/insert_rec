# Generated by Django 3.2 on 2023-09-12 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='BlogId',
        ),
    ]