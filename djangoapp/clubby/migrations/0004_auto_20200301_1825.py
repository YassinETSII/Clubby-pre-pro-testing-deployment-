# Generated by Django 3.0.3 on 2020-03-01 17:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubby', '0003_auto_20200229_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='atendees',
        ),
        migrations.AddField(
            model_name='event',
            name='atendees',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
