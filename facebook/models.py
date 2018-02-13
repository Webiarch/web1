from django.db import models

class Customer(models.Model):
    Customer_name = models.CharField(max_length=50)
    Price = models.IntegerField()
    Amount = models.IntegerField()

    def __str__(self):
        return self.Customer_name()


