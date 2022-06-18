# Generated by Django 4.0.5 on 2022-06-13 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=64)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=64, unique=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('count', models.IntegerField()),
                ('buy_price', models.IntegerField()),
                ('sell_price', models.IntegerField()),
                ('currency_type', models.CharField(blank=True, choices=[('$', '$'), ('TL', 'TL'), ('SOM', 'SOM'), ('KON', 'KON')], max_length=32, null=True)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('description', models.TextField(blank=True, max_length=512, null=True)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('category', models.ManyToManyField(to='products.productcategory')),
            ],
            options={
                'ordering': ['-datetime'],
            },
        ),
    ]