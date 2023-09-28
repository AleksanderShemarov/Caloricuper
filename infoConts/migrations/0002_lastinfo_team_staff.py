# Generated by Django 4.2.2 on 2023-09-28 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('infoConts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastinfo',
            name='team_staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
