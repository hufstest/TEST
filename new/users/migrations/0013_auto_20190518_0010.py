# Generated by Django 2.1.7 on 2019-05-17 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20190518_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='hits',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='answer',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Article'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Article'),
        ),
        migrations.AlterField(
            model_name='hit',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Article'),
        ),
        migrations.AlterField(
            model_name='like',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Article'),
        ),
        migrations.AlterField(
            model_name='taggedpost',
            name='content_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Article'),
        ),
    ]
