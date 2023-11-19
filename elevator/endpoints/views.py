from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action,api_view
from rest_framework.response import Response
from endpoints.models import ElevatorSystem, Elevator
from .serializer import ElevatorSerializer,ElevatorSystemSerializer,RequestSerializer
# @api_view(['POST'])
# def add_item

class ElevatorSystemViewset(viewsets.ModelViewSet):
    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorSystemSerializer
    @action(detail = False, methods = ['GET'])
    def by_system_name(self,request,system_id):
        '''get detail of all elevator of a system'''
        try:
            ele_system = ElevatorSystem.objects.all(elevator_system = system_id)
            serial = self.get_serializer(ele_system)
            return Response(serial.data)
        except ElevatorSystem.DoesNotExist:
            return Response({'error':'system does not exist','status':403})
    @action(detail = False,methods=['POST'])
    def request(self,request,system_id):
        '''request for elevator'''
        try:
            ele_system = ElevatorSystem.objects.filter(elevator_id = system_id)
            requested = RequestSerializer(data=request.data)
            request_from = int(requested.initial_data['request_from_floor'])
            request_to = int(requested.initial_data['request_to_floor'])
            if (ele_system[0].number_of_floors < request_from) or (request_to > ele_system[0].number_of_floors):
                return Response({'error':'enter Valid request'})
            if (request_from <=0) or (request_to <=0):
                return Response({'error':'enter Valid request'})
            assigned = None
            distance = float('inf')
            elevator = Elevator.objects.filter(elevator_system=system_id)
            for i in elevator:
                if abs((i.current_floor-request_from)) < distance:
                    distance = abs(i.current_floor-request_from)
                    assigned = i
            assigned.current_floor = request_to  
            assigned.requests += str(request_from)+',' +str(request_to)  
            if request_to - request_from > 1:
                assigned.direction = 'Up'
            elif request_to - request_from == 0:
                assigned.direction = 'Still'
            else:
                assigned.direction = 'Down'   
            assigned.save()                
            return Response({'data': 'Success'})      
        except ElevatorSystem.DoesNotExist:
            return Response({'error': 'enter valid system id'}, status=404) 
        # except Exception as e:
        #     return Response({'error':str(e)})           


             

class ElevatorViewset(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    @action(detail=True, methods=['GET'])
    def next_destiation(self, request, pk=None, system_id=None):
        '''get the next destination floor for a given elevator.'''
        try:
            elevator = self.queryset.filter(elevator_system=system_id).get(elevator_number=pk)
            temp = elevator.current_floor
            return Response({'next destination':str(temp)})
        except Exception as e:
            return Response({'error': str(e)}, status=404)
        
    @action(detail=True, methods=['GET'])
    def request_data(self,request,system_id,pk):
        '''get request of elevator'''
        try:
            elevator = self.queryset.filter(elevator_system=system_id).get(elevator_number=pk)
            response = {}
            response['elevator_system'] = system_id
            temp = elevator.requests
            #response['data'] = self.get_serializer(elevator).data
            response['requested_floors'] = str(temp)
            return Response(response)
        except Exception as e:
            return Response({'error': str(e)}, status=404)

    @action(detail=True, methods=['GET'])
    def direction(self,request,system_id,pk):
        '''get directon of elevator'''
        try:
            elevator = self.queryset.filter(elevator_system=system_id).get(elevator_number=pk)
            response = {}
            response['elevator_system'] = system_id
            temp = elevator.direction
            response['requested_floors'] = str(temp)
            return Response(response)
        except Exception as e:
            return Response({'error': str(e)}, status=404)  
        
    @action(detail=True, methods=['GET'])
    def working(self,request,system_id,pk,mark):
        '''mark elevator as working or in maintence'''
        try:
            elevator = self.queryset.filter(elevator_system=system_id).get(elevator_number=pk)
            if mark == 0:
                elevator.is_working = False
                elevator.save()  
                return Response({'message':'elevator is in maintance'})
            else:
                elevator.is_working = True
                elevator.save()  
                return Response({'message':'elevator is working'})
        except Exception as e:
            return Response({'error': str(e)}, status=404)  

    @action(detail=True, methods=['GET'])
    def door(self,request,system_id,pk,mark):
        '''mark door as open or closed'''
        try:
            elevator = self.queryset.filter(elevator_system=system_id).get(elevator_number=pk)
            if mark == 0:
                elevator.is_door_open = False
                elevator.save()
                return Response({'message':'door closed'})
            else:
                elevator.is_working = True
                elevator.save()  
                return Response({'message':'door is open'})
        except Exception as e:
            return Response({'error': str(e)}, status=404)         


