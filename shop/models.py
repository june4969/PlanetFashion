from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    link = models.URLField(blank=True)  # 링크 필드 추가
    created_at = models.DateTimeField(auto_now_add=True)
    heart = models.BooleanField(default=False)

    def __str__(self):
        return self.name

