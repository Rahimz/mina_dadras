# Generated by Django 5.1.2 on 2025-04-06 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_attachement_url_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
