# Generated by Django 5.0.1 on 2024-03-04 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actiontime',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
