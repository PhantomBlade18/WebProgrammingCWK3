# Generated by Django 3.1.1 on 2020-12-01 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_member_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(related_name='likedArticles', to='news.Member'),
        ),
    ]
