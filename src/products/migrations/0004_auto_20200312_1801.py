# Generated by Django 3.0.3 on 2020-03-12 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, height_field=150, null=True, upload_to='', width_field=150),
        ),
    ]
