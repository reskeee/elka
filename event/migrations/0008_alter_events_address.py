# Generated by Django 5.1.6 on 2025-03-02 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_events_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
