# Generated by Django 4.1.7 on 2023-04-18 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='cnmae',
            new_name='cname',
        ),
    ]
