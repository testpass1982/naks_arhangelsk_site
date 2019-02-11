# Generated by Django 2.1.2 on 2019-02-08 12:03

import ckeditor_uploader.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mainapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('short_description', models.CharField(blank=True, max_length=200, verbose_name='Краткое описание')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст')),
                ('publish_on_main_page', models.BooleanField(default=False, verbose_name='Опубликовать на главной')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'get_latest_by': ['created_date'],
                'verbose_name_plural': 'Статьи',
                'ordering': ['created_date'],
                'verbose_name': 'Статья',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'Разделы',
                'verbose_name': 'Раздел',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название контакта')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('email', models.EmailField(max_length=64, verbose_name='Адрес электронной почты')),
                ('phone', models.CharField(max_length=64, verbose_name='Телефон')),
                ('number', models.SmallIntegerField(default=0, verbose_name='Порядок вывода на сайт')),
            ],
            options={
                'verbose_name_plural': 'Контакты',
                'verbose_name': 'Контакт',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Название')),
                ('document', models.FileField(upload_to='documents/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc', 'jpg', 'jpeg'], message='Неправильный тип файла, используйте                                        PDF, DOCX, DOC, JPG, JPEG')], verbose_name='Документ')),
                ('uploaded_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Загружен')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('publish_on_main_page', models.BooleanField(default=False, verbose_name='Опубиковать на главной')),
            ],
            options={
                'verbose_name_plural': 'Документы',
                'verbose_name': 'Документ',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_code', models.CharField(max_length=30, verbose_name='Код ссылки')),
                ('title', models.CharField(max_length=60, verbose_name='Заголовок меню')),
                ('url', models.CharField(default='НЕТ', max_length=200, verbose_name='Адрес ссылки')),
            ],
            options={
                'verbose_name_plural': 'Ссылки',
                'verbose_name': 'Ссылка',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=64, verbose_name='Заголовок')),
                ('typeof', models.CharField(blank=True, max_length=64, verbose_name='Тип сообщения')),
                ('params', models.CharField(blank=True, max_length=512, verbose_name='Параметры сообщения')),
                ('sender_email', models.EmailField(blank=True, max_length=64, verbose_name='Адрес электронной почты')),
                ('sender_phone', models.CharField(blank=True, max_length=64, verbose_name='Телефон')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата получения')),
                ('status', models.IntegerField(choices=[(0, 'new'), (1, 'registered'), (2, 'added_to_sending_queue'), (3, 'notify_sent')], default=0, verbose_name='Статус')),
            ],
            options={
                'verbose_name_plural': 'Сообщения',
                'verbose_name': 'Сообщение',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('short_description', models.CharField(blank=True, max_length=200, verbose_name='Краткое описание')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст')),
                ('publish_on_main_page', models.BooleanField(default=False, verbose_name='Опубликовать на главной')),
                ('publish_on_news_page', models.BooleanField(default=False, verbose_name='Опубликовать в ленте новостей')),
                ('secondery_main', models.BooleanField(default=False, verbose_name='Опубликовать на главной как новость без картинки')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
            ],
            options={
                'get_latest_by': ['created_date'],
                'verbose_name_plural': 'Страницы',
                'ordering': ['created_date'],
                'verbose_name': 'Страница',
            },
        ),
        migrations.CreateModel(
            name='PostPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='upload/', verbose_name='изображение')),
                ('title', models.CharField(blank=True, default=mainapp.models.get_image_filename, max_length=64, verbose_name='название')),
                ('position', models.PositiveIntegerField(default=0, verbose_name='Позиция')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='mainapp.Post', verbose_name='новость')),
            ],
            options={
                'verbose_name_plural': 'Фотографии',
                'ordering': ['position'],
                'verbose_name': 'Фото',
            },
        ),
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=64, verbose_name='Название')),
                ('org', models.CharField(blank=True, max_length=120, verbose_name='Организация')),
                ('typeof', models.CharField(blank=True, max_length=64, verbose_name='Тип')),
                ('params', models.CharField(blank=True, max_length=999, verbose_name='Параметры')),
                ('created_date', models.DateField(blank=True, verbose_name='Дата получения')),
                ('status', models.IntegerField(choices=[(0, 'new'), (1, 'published')], default=0, verbose_name='Статус')),
            ],
            options={
                'verbose_name_plural': 'Записи реестра',
                'verbose_name': 'Запись реестра',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='Фотография')),
                ('name', models.CharField(max_length=120, verbose_name='ФИО')),
                ('job', models.CharField(max_length=120, verbose_name='Должность')),
                ('experience', models.CharField(blank=True, max_length=500, verbose_name='Опыт работы')),
                ('priority', models.SmallIntegerField(default=0, verbose_name='Приоритет')),
            ],
            options={
                'verbose_name_plural': 'Сотрудники',
                'verbose_name': 'Сотрудник',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'Тэги',
                'verbose_name': 'Тэг',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='mainapp.Tag', verbose_name='Тэги'),
        ),
        migrations.AddField(
            model_name='document',
            name='post',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.Post', verbose_name='Страница'),
        ),
        migrations.AddField(
            model_name='document',
            name='tags',
            field=models.ManyToManyField(blank=True, to='mainapp.Tag', verbose_name='Тэги'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='mainapp.Tag', verbose_name='Тэги'),
        ),
    ]
