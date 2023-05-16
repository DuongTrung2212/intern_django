# Generated by Django 4.2 on 2023-05-16 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tour', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='staff', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='decription',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour', to='tour.tour'),
        ),
    ]