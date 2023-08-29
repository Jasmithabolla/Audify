# Generated by Django 5.0.dev20230120115851 on 2023-07-02 10:40

import converter.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('converter', '0006_audiofile_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiofile',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
