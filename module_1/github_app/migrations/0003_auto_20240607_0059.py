# Generated by Django 3.2.12 on 2024-06-07 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github_app', '0002_auto_20240606_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='githubapp',
            name='name',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='githubapp',
            name='private_repo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='githubapp',
            name='public_repo',
            field=models.BooleanField(default=True),
        ),
    ]
