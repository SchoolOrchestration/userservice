# Generated by Django 2.0 on 2018-02-28 12:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_auto_20180228_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]