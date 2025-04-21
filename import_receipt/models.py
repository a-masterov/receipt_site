from django.db import models


class Store(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=255)
    rec_id = models.CharField(max_length=64)
    location = models.CharField(max_length=255)


class Currency(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=5)


class Receipt(models.Model):
    def __str__(self):
        return self.number
    store = models.ForeignKey(Store, on_delete=models.SET_NULL)
    number = models.CharField(max_length=64)
    date_time = models.DateTimeField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)


class Category(models.Model):
    def __str__(self):
        return self.name

    def get_default_category(self):
        category, _ = self.objects.get_or_create(name="Others")
        return category.id
    name = models.CharField(max_length=127, unique=True)


class Items(models.Model):
    def __str__(self):
        return self.description
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    tax_base = models.DecimalField(max_digits=9, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=4, decimal_places=2)
    tax = models.DecimalField(max_digits=9, decimal_places=2)
    total = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=Category.get_default_category,
                                 null=False, blank=False)
    receipt = models.ForeignKey(Receipt, on_delete=models.SET_NULL)
