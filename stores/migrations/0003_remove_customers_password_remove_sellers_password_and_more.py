# Generated by Django 4.2.5 on 2024-02-12 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_alter_customers_owner_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='password',
        ),
        migrations.RemoveField(
            model_name='sellers',
            name='password',
        ),
        migrations.AddField(
            model_name='customers',
            name='birthdate',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='sellers',
            name='birthdate',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='owner_id',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='sellers',
            name='owner_id',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
