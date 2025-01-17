from django.db import models
from datetime import date

# Create your models here.
class Trainer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    level = models.IntegerField(default=1)
    birth_date = models.DateField(null=True, blank=True)
    trainer_picture = models.ImageField(upload_to="trainers_images", null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def age(self):
        if self.birth_date:
            today = date.today()
            return today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
            )
        return None
    
class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False)
    POKEMON_TYPES ={
        ('A','Agua'),
        ('F','Fuego'),
        ('T','Tierra'),
        ('P','Planta'),
        ('E','Elèctrico'),
        ('L','Lagartija'),
    }
    type = models.CharField(max_length=30, choices=POKEMON_TYPES, null=False)
    weight = models.DecimalField(max_digits=6, decimal_places=4)
    height = models.DecimalField(max_digits=6, decimal_places=4)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(upload_to="pokemon_images")
    
    def __str__(self):
        return self.name
    