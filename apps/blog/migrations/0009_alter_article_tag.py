# Generated by Django 4.1.3 on 2022-11-18 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_tag_article_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, to='blog.tag', verbose_name='Теги'),
        ),
    ]
