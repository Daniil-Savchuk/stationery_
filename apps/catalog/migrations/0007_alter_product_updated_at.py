# Generated by Django 4.1.3 on 2022-12-29 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_remove_product_created_at_alter_product_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=0, verbose_name='Дата изменения'),
        ),
    ]
