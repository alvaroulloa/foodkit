# Generated by Django 3.0.7 on 2020-06-09 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='This is a test.'),
            preserve_default=False,
        ),
    ]