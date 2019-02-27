# Generated by Django 2.1.5 on 2019-02-20 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='url_code',
            field=models.CharField(blank=True, default='НЕ УКАЗАН', max_length=30, verbose_name='Код ссылки'),
        ),
        migrations.AddField(
            model_name='post',
            name='url_code',
            field=models.CharField(blank=True, default='НЕ УКАЗАН', max_length=30, verbose_name='Код ссылки'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=60, verbose_name='Заголовок ссылки'),
        ),
    ]