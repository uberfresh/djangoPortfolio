# Generated by Django 3.2.4 on 2021-06-06 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmessage',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contactmessage',
            old_name='last_name',
            new_name='subject',
        ),
    ]