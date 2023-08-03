from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    title = models.CharField(max_length=200)
    # details = models.ManyToManyField('Detail')

    def __str__(self):
        return self.title

    def selected_product(self):
        return Selected.objects.filter(select=self.id)

    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежда'
        ordering = ['title']


class Detail(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    brand = models.CharField(max_length=200)
    cost = models.PositiveIntegerField()

    def __str__(self):
        return self.product


class Selected(models.Model):
    select = models.ForeignKey("Product", on_delete=models.CASCADE)




