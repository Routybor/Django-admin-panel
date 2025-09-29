from django.db import models
from django.conf import settings


CON = settings.CONSTANTS


class Computer(models.Model):
    title = models.TextField(
        verbose_name="Название",
        max_length=CON.FIELD_LEN,
        choices=CON.TITLE_CHOICES,
        default=CON.TITLE_CHOICES[0][0],
    )
    link = models.TextField(
        verbose_name="Ссылка",
    )
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=10,
        decimal_places=2,
    )
    cpu = models.CharField(
        verbose_name="Процессор",
        max_length=CON.FIELD_LEN,
    )
    gpu = models.CharField(
        verbose_name="Видеокарта",
        max_length=CON.FIELD_LEN,
    )
    ram = models.CharField(
        verbose_name="Оперативная память",
        max_length=CON.FIELD_LEN,
    )
    motherboard = models.CharField(
        verbose_name="Материнская плата",
        max_length=CON.FIELD_LEN,
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )
    photo = models.BinaryField(
        verbose_name="Фото",
        editable=True,
    )

    class Meta:
        verbose_name = "Компьютер"
        verbose_name_plural = "Компьютеры"

    def __str__(self):
        return self.title
