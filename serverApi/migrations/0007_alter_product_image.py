# Generated by Django 5.0.6 on 2024-06-11 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serverApi', '0006_product_image_alter_cart_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(default='https://img.freepik.com/free-vector/shopping-cart-realistic_1284-6011.jpg?size=338&ext=jpg&ga=GA1.1.1141335507.1718064000&semt=ais_user', max_length=10000),
        ),
    ]