from rest_framework import serializers
from .models import Elevator,ElevatorSystem, Request
from rest_framework.response import Response

class ElevatorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Elevator
        fields = '__all__'

class ElevatorSystemSerializer(serializers.ModelSerializer):

    elevators = serializers.SerializerMethodField()
    class Meta:
        model = ElevatorSystem
        fields = '__all__' 
       
    def get_elevators(self,obj):
        elevator = Elevator.objects.filter(elevator_system = obj)
        return  ElevatorSerializer(elevator,many = True).data

    def create(self, obj):
        
        system = ElevatorSystem.objects.create(**obj)
        number_of_elevators = obj['number_of_elevator']
        number_of_floor = obj['number_of_floors']
        if number_of_floor <= 1:
            raise Exception({'error':'enter valid floors'})
        if number_of_elevators <= 0:
            raise Exception({'error':'enter valid elevators'})

        if number_of_elevators:
            for i in range(1, number_of_elevators + 1):
                Elevator.objects.create(elevator_system=system, elevator_number=i)

        return system        
class RequestSerializer(serializers.ModelSerializer):  

    class Meta:
        model = Request
        fields = '__all__'  

       
