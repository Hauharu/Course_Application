# Generated by Django 5.1.2 on 2024-11-24 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0002_comment_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='updated_date',
        ),
        migrations.RemoveField(
            model_name='like',
            name='active',
        ),
        migrations.RemoveField(
            model_name='like',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='like',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='like',
            name='updated_date',
        ),
    ]
