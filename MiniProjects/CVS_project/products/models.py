from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=20)
    manager = models.CharField(max_length=20)
    image = models.ImageField(default='/media/ghost.jpeg')

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Incharge(models.Model):
    SEX_SELECT = (
        ('M', 'Male'),
        ('F', 'Female'),
        )
    name = models.CharField(max_length=10)
    sex = models.CharField(max_length=1, choices=SEX_SELECT)
    age = models.IntegerField()
    goods = models.ManyToManyField(Store, through='Item')

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(default='/media/ghost.jpeg')
    stock = models.IntegerField()
    category = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    incharge = models.ForeignKey(Incharge, on_delete=models.CASCADE)

    class Meta:
        ordering = ('category',)

    # def get_image(self):
    #     if self.image:
    #         return self.image.url
    #     else:
    #         return '/media/ghost.jpeg'