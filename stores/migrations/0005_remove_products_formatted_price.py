# Generated by Django 4.2.5 on 2024-02-06 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_alter_categories_options_alter_customers_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='formatted_price',
        ),
    ]
