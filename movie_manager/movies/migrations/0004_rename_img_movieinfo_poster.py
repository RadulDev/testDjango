# Generated by Django 4.2.10 on 2024-02-13 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movieinfo_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movieinfo',
            old_name='img',
            new_name='poster',
        ),
    ]
