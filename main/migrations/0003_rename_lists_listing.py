# Generated by Django 4.2.3 on 2023-09-03 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_photo'),
        ('main', '0002_lists_brand_lists_color_lists_description_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lists',
            new_name='Listing',
        ),
    ]
