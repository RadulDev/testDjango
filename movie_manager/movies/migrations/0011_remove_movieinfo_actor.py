# Generated by Django 4.2.10 on 2024-02-15 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_remove_movieinfo_actor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movieinfo',
            name='actor',
        ),
    ]
