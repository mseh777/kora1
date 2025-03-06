# Generated by Django 5.1.6 on 2025-02-27 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_posts_card_location_delete_championships'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professionals',
            name='user',
        ),
        migrations.RemoveField(
            model_name='social_media',
            name='user',
        ),
        migrations.RemoveField(
            model_name='transfers',
            name='user',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='views',
        ),
        migrations.AlterField(
            model_name='posts',
            name='card_location',
            field=models.CharField(choices=[('1', 'Card left small'), ('2', 'Card center'), ('3', 'Card right small'), ('4', 'Card one'), ('5', 'Card two'), ('6', 'Card three'), ('7', 'Card Boss'), ('8', 'Card four'), ('9', 'Card five'), ('10', 'Card sex'), ('11', 'Card seven'), ('12', 'Card eight'), ('13', 'Card nine'), ('other', 'Other'), ('gust_post', 'Gust_post'), ('champ', 'Championships'), ('trans', 'Transfers')], default='other', help_text='حدد مكان عرض البوست', max_length=30),
        ),
        migrations.DeleteModel(
            name='PostView',
        ),
        migrations.DeleteModel(
            name='Professionals',
        ),
        migrations.DeleteModel(
            name='Social_Media',
        ),
        migrations.DeleteModel(
            name='Transfers',
        ),
    ]
