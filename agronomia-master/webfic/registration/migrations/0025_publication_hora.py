# Generated by Django 2.1.3 on 2019-07-28 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0024_auto_20190728_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='hora',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Hora'),
        ),
    ]
