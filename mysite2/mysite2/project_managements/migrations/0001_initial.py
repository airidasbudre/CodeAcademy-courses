# Generated by Django 4.1.5 on 2023-01-28 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('surname', models.CharField(max_length=200, verbose_name='Surname')),
                ('company', models.CharField(max_length=200, verbose_name='Company')),
                ('email', models.CharField(max_length=200, verbose_name='Email')),
                ('phone', models.IntegerField(verbose_name='Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('surname', models.CharField(max_length=200, verbose_name='Surname')),
                ('position', models.CharField(max_length=200, verbose_name='Surname')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formating_date', models.DateField(blank=True, null=True, verbose_name='Formating Date')),
                ('amount', models.FloatField(max_length=11, verbose_name='Amount')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('note', models.CharField(max_length=200, verbose_name='Note')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=200, verbose_name='Project Name')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End date')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_managements.client')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_managements.employee')),
                ('invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_managements.invoice')),
                ('work', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_managements.work')),
            ],
        ),
    ]