# Generated by Django 2.1.3 on 2019-03-09 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_auto_20190309_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='status',
            new_name='estatus',
        ),
    ]
