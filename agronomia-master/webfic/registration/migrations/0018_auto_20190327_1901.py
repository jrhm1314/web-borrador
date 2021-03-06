# Generated by Django 2.1.3 on 2019-03-27 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0017_auto_20190323_0051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ['-created']},
        ),
        migrations.RemoveField(
            model_name='publication',
            name='order',
        ),
        migrations.AddField(
            model_name='publication',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Nombre de usuario'),
        ),
    ]
