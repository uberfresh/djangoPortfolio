# Generated by Django 3.2.4 on 2021-06-20 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210620_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutuser',
            name='is_previously_logged',
            field=models.BooleanField(default=False),
        ),
    ]