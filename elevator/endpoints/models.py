from django.db import models

# Create your models here.
class ElevatorSystem(models.Model):
    elevator_id = models.AutoField(primary_key=True)
    number_of_elevator = models.IntegerField(default = 1)
    number_of_floors = models.IntegerField(default = 2)


class Elevator(models.Model):
    elevator_system = models.ForeignKey('ElevatorSystem',on_delete = models.CASCADE,db_column = 'elevator_id')
    elevator_number = models.IntegerField()
    current_floor = models.IntegerField(default = 1)
    is_door_open = models.BooleanField(default = True)
    direction = models.CharField(max_length = 20,default = 'still')     
    is_working = models.BooleanField(default = True)
    requests = models.CharField(max_length = 100)

class Request(models.Model):
    requested_from_floor = models.IntegerField()
    requested_to_floor = models.IntegerField()    