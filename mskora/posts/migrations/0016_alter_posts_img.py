# Generated by Django 5.1.6 on 2025-03-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_matchday_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='img',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='imgposts/'),
        ),
    ]
