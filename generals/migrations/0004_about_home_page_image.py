# Generated by Django 5.1.2 on 2025-04-11 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generals', '0003_about_addition_about_addition_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='home_page_image',
            field=models.ImageField(blank=True, null=True, upload_to='about/', verbose_name='Image in home page'),
        ),
    ]
