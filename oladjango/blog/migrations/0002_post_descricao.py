# Generated by Django 2.0.13 on 2019-08-13 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='descricao',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
