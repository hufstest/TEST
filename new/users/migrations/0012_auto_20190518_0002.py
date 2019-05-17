# Generated by Django 2.1.7 on 2019-05-17 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20190517_2359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hit',
            old_name='created_at',
            new_name='day',
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
        migrations.AlterUniqueTogether(
            name='hit',
            unique_together={('ip', 'article', 'day')},
        ),
    ]
