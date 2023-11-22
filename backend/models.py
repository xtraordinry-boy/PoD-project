from django.db import models

class User(models.Model):
  username = models.CharField(max_length=255, unique=True)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=255)

class Store(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  description = models.TextField()

class Design(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  store = models.ForeignKey(Store, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  description = models.TextField()
  image = models.ImageField(upload_to='designs')

class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  design = models.ForeignKey(Design, on_delete=models.CASCADE)
  product_type = models.CharField(max_length=255) # e.g., T-shirt, mug, phone case
  status = models.CharField(max_length=255) # e.g., pending, processing, shipped, delivered
  order_date = models.DateTimeField(auto_now_add=True)

