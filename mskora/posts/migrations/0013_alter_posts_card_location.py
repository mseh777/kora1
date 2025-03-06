# Generated by Django 5.1.6 on 2025-02-28 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_alter_posts_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='card_location',
            field=models.CharField(choices=[('1', 'Card left small'), ('2', 'Card center'), ('3', 'Card right small'), ('4', 'Card one'), ('5', 'Card two'), ('6', 'Card three'), ('7', 'Card Boss'), ('8', 'Card four'), ('9', 'Card five'), ('10', 'Card sex'), ('11', 'Card seven'), ('12', 'Card eight'), ('13', 'Card nine'), ('news', 'News'), ('gust_post', 'Gust_post'), ('champ', 'Championships'), ('analytics', 'Analytics'), ('trans', 'Transfers'), ('social', 'Social_Media'), ('prof', 'Professionals'), ('another_sports', 'Another_Sports')], default='other', help_text='حدد مكان عرض البوست', max_length=30),
        ),
    ]
