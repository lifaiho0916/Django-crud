# Generated by Django 4.2.1 on 2023-05-29 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='eemial',
            new_name='eemail',
        ),
    ]
