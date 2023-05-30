# Generated by Django 4.2.1 on 2023-05-04 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=0)),
                ('order_number', models.IntegerField(default=0)),
                ('user_name', models.CharField(max_length=20)),
                ('user_lastname', models.CharField(max_length=30)),
                ('id_manager', models.IntegerField(default=0)),
            ],
        ),
    ]
