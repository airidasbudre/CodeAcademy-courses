# Generated by Django 4.1.5 on 2023-01-17 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_car_model_options_alter_cars_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderline',
            options={'verbose_name': 'Orderline', 'verbose_name_plural': 'Orderlines'},
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.FloatField(verbose_name='Price'),
        ),
    ]
