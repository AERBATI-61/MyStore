from django.contrib.auth.models import User
from django.db import models
from products.models import Product

currency_units = (
    ('$', '$'),
    ('TL', 'TL'),
    ('SOM', 'SOM'),
    ('KON', 'KON'),
)

money_banks = (
    ('Money', 'Money'),
    ('Bank', 'Bank'),
    ('Paid', 'Paid'),
)


class Tax(models.Model):
    tax                     = models.IntegerField(unique=True)

    def __str__(self):
        return str(f'{self.tax} %')


class City(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f"{self.id} ---  {self.name}"




class Seller(models.Model):
    seller          = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image           = models.ImageField(upload_to='customer_images/', null=True, blank=True)
    email           = models.EmailField()
    phone           = models.CharField(max_length=32)
    city            = models.ForeignKey(City, on_delete=models.CASCADE, related_name="cities",)
    address         = models.TextField()
    description     = models.TextField(null=True,blank=True)
    date            = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.seller}"







class Customer(models.Model):
    name                = models.CharField(max_length=64,unique=True)
    image               = models.ImageField(upload_to='customer_images/', null=True, blank=True)
    phone_number        = models.CharField(max_length=16,null=True,blank=True)
    email               = models.EmailField(null=True,blank=True)
    address             = models.TextField(null=True,blank=True)
    belongs_to_seller   = models.ForeignKey(Seller, on_delete=models.CASCADE,related_name='belongs_to_seller')
    description         = models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.name}"





class Invoice(models.Model):
    inv_no                      = models.CharField(max_length=128, null=True, blank=True, unique=True)
    product                    = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    customer                    = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    seller                      = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='invoice_user')
    datetime                    = models.DateTimeField()
    tax                         = models.ForeignKey(Tax, on_delete=models.CASCADE)
    count                       = models.IntegerField()
    description                 = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.seller.seller} - For - {self.customer}"







class SoldProduct(models.Model):
    product                     = models.ForeignKey(Product, on_delete=models.CASCADE)
    datetime                    = models.DateTimeField(auto_now=True)
    seller                      = models.ForeignKey(Seller, on_delete=models.CASCADE)
    customer                    = models.ForeignKey(Customer, on_delete=models.CASCADE)
    invoice                     = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.product.name}"








class Payment(models.Model):
    invoice                     = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    seller                      = models.ForeignKey(Seller, on_delete=models.CASCADE)
    customer                    = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    money_bank                  = models.CharField(max_length=32, choices=money_banks, blank=True, null=True)
    amount                      = models.IntegerField()
    currency_type               = models.CharField(max_length=32, choices=currency_units, blank=True, null=True)
    description                 = models.TextField(null=True, blank=True)
    date                        = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.seller.seller} Customer: {self.customer.name}"