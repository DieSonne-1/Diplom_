# Generated by Django 4.2.17 on 2024-12-16 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_image_alter_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
