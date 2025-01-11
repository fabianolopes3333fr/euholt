# Generated by Django 5.1.4 on 2025-01-11 17:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('financial', '0001_initial'),
        ('scheduling', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='scheduling',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scheduling.scheduling'),
        ),
    ]