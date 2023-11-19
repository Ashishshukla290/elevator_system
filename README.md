Elevator management system using Django Rest Framework

Installation

    Running locally
        Clone the repository
        Change directory to elevator
        Create a virtual environment        
        Activate the virtual environment and install the requirements
        Install Required Libraries
        Run the server

     - git clone
     - cd elevator
     - virtualenv venv
     - source venv/bin/activate
     - pip install asgiref==3.7.1
     - pip install django==4.2.1
     - pip install djangorestframework==3.14.0
     - pip install psycopg2-binary==2.9.6
     - pip install pytz==2023.3
     - pip install sqlparse==0.4.4
     - python manage.py runserver or python3 manage.py runserver


Thought Process

My initial idea was to create a single elevator system and number of elevators = n, number of floors = 2n-1.But I discarded the idea as I realised that the above approach might not be scalable for this app. Instead i created two tables ElevatorSystem and Elevator. User can create multiple system by calling api and specify number_of_elevator and number_of_floors in request body. It will add a ElevatorSystem in table and will add number_of_elevator in Elevator table with Forign_key = ElevatorSystem.

File Structure  
```
  ├── README.md
  |── elevator
  |  ├── elevator
  │   ├── __init__.py
  │   ├── asgi.py
  │   ├── settings.py
  │   ├── urls.py
  │   └── wsgi.py
  |  ├── endpoints
  │   ├── __init__.py
  │   ├── admin.py
  │   ├── apps.py
  │   ├── migrations
  │   ├── models.py
  │   ├── serializer.py
  │   ├── tests.py
  │   ├── urls.py
  │   └── views.py
  ├── manage.py
```


Usage

    Create new elevator system
        Endpoint: /elevator-systems/
        Method : POST
        Request body:

    {
        "number_of_elevator": "3",
        "number_of_floors": "9"
    }

Get elevator system info

    Endpoint: /elevator-systems/<system-id>
    Method: GET
    Lists all the elevators in the system and their current status

Create elevator request

    Endpoint: /elevator-systems/<system-id>/request/
    Method : POST
    Request body:
```
{
  "requested_from_floor": "3",
  "requested_to_floor": "9"
}
```
Get elevator request data

    Endpoint: /elevator-systems/<system-id>/<elevator-id>/request-data/
    Method : GET
    Lists all the requests made to the elevator

Get elevator next destination

    Endpoint: /elevator-systems/<system-id>/<elevator-id>/next/
    Method: GET
    Responds with the next_stop of elevator.
    
Get elevator direction

    Endpoint: /elevator-systems/<system-id>/<elevator-id>/direction/
    Method: GET
    Responds with the direction of elevator.

Open/close elevator door 

    Endpoint: /elevator-systems/<system-id>/<elevator-id>/1 or 0/door/
    Method: GET
    Responds with the direction of elevator.
    1 is want to open door.
    0 if want to close the door.

Change working status of elevator

    Endpoint: /elevator-systems/<system-id>/<elevator-id>/1 or 0/isworking/
    Method: GET
    Responds with the direction of elevator.
    1 if elevator is working.
    0 if elevator is in maintenance.    
    
    

