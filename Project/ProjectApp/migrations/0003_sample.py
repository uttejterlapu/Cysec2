# Generated by Django 5.0.3 on 2024-04-03 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0002_project_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('des', models.TextField()),
            ],
        ),
    ]
