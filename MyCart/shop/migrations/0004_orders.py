# Generated by Django 3.2.4 on 2021-06-08 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=7000)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=130)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=15)),
            ],
        ),
    ]
