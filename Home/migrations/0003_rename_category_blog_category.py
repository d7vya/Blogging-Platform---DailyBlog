# Generated by Django 3.2.25 on 2025-01-12 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_tag_tag_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='Category',
            new_name='category',
        ),
    ]
