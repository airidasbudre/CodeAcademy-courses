# Generated by Django 4.1.5 on 2023-01-26 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_alter_orderline_order_alter_orderline_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='quantity',
            field=models.IntegerField(verbose_name='Quantity'),
        ),
    ]
