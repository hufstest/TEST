# Generated by Django 2.1.7 on 2019-05-17 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20190517_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Article')),
            ],
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
