# Generated by Django 5.1.2 on 2024-10-28 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_attachement_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('image', 'Image gallery'), ('mix', 'Mix content')], default='image', max_length=10, verbose_name='Type'),
        ),
    ]
