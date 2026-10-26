from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название команды")
    country = models.CharField(max_length=100, verbose_name="Страна")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Size(models.Model):
    name = models.CharField(max_length=10, verbose_name="Размер")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, verbose_name="Команда")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория")
    sizes = models.ManyToManyField(Size, blank=True, verbose_name="Доступные размеры")
    
    in_stock = models.BooleanField(default=True, verbose_name="В наличии")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class Customer(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews", verbose_name="Товар")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Покупатель")
    text = models.TextField(verbose_name="Текст отзыва")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name="Оценка (1-5)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Отзыв от {self.customer} на {self.product}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"