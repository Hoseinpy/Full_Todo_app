# Generated by Django 5.0.4 on 2024-04-23 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_todomodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=100)),
        ),
    ]