# Generated by Django 5.0 on 2023-12-19 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='category',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]
