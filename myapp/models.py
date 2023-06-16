from django.db import models

# Create your models here.
STATUS=(
   ('tayyorlanyapti','tayyorlanyapti'),
    ("tayyor bo'ldi","tayyor bo'ldi")
)
class Dostavka(models.Model):
    name = models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    count=models.PositiveBigIntegerField(default=1,null=True,blank=True)
    price=models.PositiveBigIntegerField(default=0,null=True,blank=True)
    all_price=models.PositiveBigIntegerField(default=0,null=True,blank=True)
    location=models.CharField(max_length=50)
    status=models.CharField(max_length=100, choices=STATUS,default="tayyorlanyapti")
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
      ordering=["id"]
      verbose_name="Dostavka"
      verbose_name_plural="Dostavka"

    def __str__(self):
      return f"{self.name} {self.title} buyurdi"
          

     
    def get_all_price(self):
      return self.count*self.price    