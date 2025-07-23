from django.db import models


class Item(models.Model):
    CATEGORIES = [
        ('گازی', 'Gas'),
        ('برقی', 'Electric'),
    ]
    CATEGOTY_LIST = ['برقی', 'گازی']
    title = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='media/', default='media/products/default.png', blank=True)
    catalog = models.ImageField(upload_to='media/', default='media/catalogs/default.png', blank=True)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.title}'
    
    
    
class Province(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="cities")
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('province', 'name')

    def __str__(self):
        return f"{self.name} ({self.province.name})"


class Technician(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="technicians")
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    mobile = models.JSONField(default=list, blank=True)  # Stores as a list in PostgreSQL/MySQL
    phone = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment #{self.id} - {self.created_at.strftime('%Y-%m-%d')}"