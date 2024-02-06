# Generated by Django 4.2.5 on 2024-02-06 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0005_remove_products_formatted_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=9),
        ),
    ]
