from django.db import models

class Bow(models.Model):
    name = models.CharField('Название', max_length=100)
    color = models.CharField('Цвет', max_length=80)
    description = models.CharField('Описание', max_length=200)
    quantity = models.IntegerField('Количество', default=30)
    price = models.IntegerField('Цена', default=350)
    photo1 = models.ImageField('Фото', upload_to='static/main/img', blank=True)

    def __str__(self):
        return self.name

