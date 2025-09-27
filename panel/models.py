from django.db import models

class Computer(models.Model):
    title = models.CharField("Название", max_length=255)
    link = models.TextField("Ссылка", blank=True, null=True)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2, blank=True, null=True)
    cpu = models.CharField("Процессор", max_length=255, blank=True, null=True)
    gpu = models.CharField("Видеокарта", max_length=255, blank=True, null=True)
    ram = models.CharField("Оперативная память", max_length=255, blank=True, null=True)
    motherboard = models.CharField("Материнская плата", max_length=255, blank=True, null=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    photo = models.BinaryField("Фото", blank=True, null=True, editable=True)

    class Meta:
        verbose_name = "Компьютер"
        verbose_name_plural = "Компьютеры"

    def __str__(self):
        return self.title
