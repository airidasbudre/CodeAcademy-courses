# Generated by Django 4.1.5 on 2023-01-31 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0011_alter_orderline_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='reader',
        ),
        migrations.AddField(
            model_name='cars',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='cars',
            name='photo',
            field=models.ImageField(null=True, upload_to='cars', verbose_name='Photo'),
        ),
        migrations.AddField(
            model_name='order',
            name='duration',
            field=models.DateTimeField(null=True, verbose_name='Duration'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cars',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.cars'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('p', 'Patvirtinta'), ('v', 'Vykdoma'), ('a', 'Atšaukta'), ('i', 'Įvykdyta')], default='p', help_text='Statusas', max_length=1),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]