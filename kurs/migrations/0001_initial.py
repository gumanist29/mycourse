# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-10-22 18:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Отрасли',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=150, null=True)),
            ],
            options={
                'verbose_name': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Phone', 'PHONE'), ('Facebook', 'FACEBOOK'), ('Email', 'EMAIL')], default='Phone', max_length=20)),
                ('value', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('logo', models.CharField(max_length=150)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='kurs.Category')),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='kurs.Course'),
        ),
        migrations.AddField(
            model_name='branch',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='kurs.Course'),
        ),
    ]