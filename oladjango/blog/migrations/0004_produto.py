# Generated by Django 2.0.13 on 2019-08-15 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_resumo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('marca', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]