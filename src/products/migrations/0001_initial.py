# Generated by Django 3.1.6 on 2022-03-28 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('label', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('gtin', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True)),
                ('expirationDate', models.DateField()),
            ],
        ),
    ]
