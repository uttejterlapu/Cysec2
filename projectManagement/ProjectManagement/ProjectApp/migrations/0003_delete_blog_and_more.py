# Generated by Django 5.0.3 on 2024-03-30 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0002_blog'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='assigned_users',
            new_name='team_members',
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=20),
        ),
    ]
