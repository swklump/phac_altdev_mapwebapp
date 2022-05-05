# Generated by Django 3.2.7 on 2022-04-29 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ALIGN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EMAIL', models.CharField(max_length=255)),
                ('ORDER', models.IntegerField()),
                ('LAT', models.CharField(max_length=255)),
                ('LON', models.CharField(max_length=255)),
                ('TEXTINPUT', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='INT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EMAIL', models.CharField(max_length=255)),
                ('LAT', models.CharField(max_length=255)),
                ('LON', models.CharField(max_length=255)),
                ('TEXTINPUT', models.CharField(max_length=255)),
            ],
        ),
    ]