# Generated by Django 5.1.6 on 2025-02-28 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_posts_card_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
