# Generated by Django 5.1.6 on 2025-02-26 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='card_location',
            field=models.CharField(choices=[('1', 'Card left small'), ('2', 'Card center'), ('3', 'Card right small'), ('4', 'Card one'), ('5', 'Card two'), ('6', 'Card three'), ('7', 'Card Boss'), ('8', 'Card four'), ('9', 'Card five'), ('10', 'Card sex'), ('11', 'Card seven'), ('12', 'Card eight'), ('13', 'Card nine'), ('other', 'Other'), ('gust_post', 'Gust_post'), ('Championships', 'Championships'), ('Transfers', 'Transfers'), ('Social_Media', 'Social_Media'), ('Professionals', 'Professionals')], default='other', help_text='حدد مكان عرض البوست', max_length=20),
        ),
    ]
