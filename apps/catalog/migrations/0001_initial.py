# Generated by Django 4.1.3 on 2023-01-02 20:17

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг (чпу)')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Цена')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг (чпу)')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='catalog/category/', verbose_name='Изображение')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='catalog.category', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
    ]
