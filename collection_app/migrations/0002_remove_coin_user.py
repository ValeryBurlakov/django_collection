# Generated by Django 5.0.3 on 2024-03-21 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coin',
            name='user',
        ),
    ]
