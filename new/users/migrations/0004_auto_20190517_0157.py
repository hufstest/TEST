# Generated by Django 2.1.7 on 2019-05-16 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_article_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='answer_user_set',
        ),
        migrations.RemoveField(
            model_name='article',
            name='comment_user_set',
        ),
        migrations.RemoveField(
            model_name='article',
            name='like_user_set',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.CharField(max_length=300),
        ),
    ]
