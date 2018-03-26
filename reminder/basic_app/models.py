from django.db import models

# Create your models here.
class truck(models.Model):
    truck_number=models.IntegerField()
    licance_id=models.IntegerField()
    licence_exp=models.DateField()
    fitness_id=models.IntegerField()
    fitness_exp=models.DateField()
    read=models.BooleanField(default=False)


    def __str__(self):
        return "Truck No: "+str(self.truck_number)

