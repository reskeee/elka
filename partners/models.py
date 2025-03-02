from django.db import models


class Partners(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название партнёра")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    main_image = models.ImageField(upload_to='partners_main_images/', verbose_name="Основное изображение", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Партнёр"
        verbose_name_plural = "Партнёры"


class PartnersImage(models.Model):
    product = models.ForeignKey(Partners, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/', verbose_name="Дополнительное изображение")

    def __str__(self):
        return f"Дополнительное изображение для {self.product.name}"

    class Meta:
        verbose_name = "Дополнительное изображение партенра"
        verbose_name_plural = "Дополнительные изображения партнеров"