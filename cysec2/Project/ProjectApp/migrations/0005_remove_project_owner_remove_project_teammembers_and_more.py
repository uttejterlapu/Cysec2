# Generated by Django 5.0.3 on 2024-04-03 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0004_projectcreate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='project',
            name='teammembers',
        ),
        migrations.DeleteModel(
            name='sample',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]