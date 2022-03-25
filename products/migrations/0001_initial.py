# Generated by Django 3.2.7 on 2022-03-25 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prd_title', models.CharField(max_length=200)),
                ('prd_cat', models.CharField(max_length=100)),
                ('prd_price', models.IntegerField()),
                ('prd_desc', models.TextField()),
                ('prd_img', models.ImageField(upload_to='pics')),
                ('prd_keyword', models.CharField(max_length=100, null=True)),
                ('prd_quantity', models.IntegerField(default=0)),
            ],
        ),
    ]
