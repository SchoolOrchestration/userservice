# Generated by Django 2.0 on 2018-02-28 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20180228_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Permission')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='teampermissions',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Team'),
        ),
        migrations.AddField(
            model_name='team',
            name='permissions',
            field=models.ManyToManyField(through='api.TeamPermissions', to='api.Permission'),
        ),
    ]
