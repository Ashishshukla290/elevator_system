from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ElevatorSystemViewset,ElevatorViewset
router = DefaultRouter()
router.register(r'elevator-system',ElevatorSystemViewset,basename = 'elevator-system')
urlpatterns = [
    path('',include(router.urls)),
    path('elevator-systems/<int:system_id>/', ElevatorSystemViewset.as_view({'get': 'by_system_name'}),
         name='elevator-systems-by-name'),
    path('elevator-system/<int:system_id>/<int:pk>/next/',
         ElevatorViewset.as_view({'get': 'next_destiation'}), name='next-destiation'),
    path('elevator-system/<int:system_id>/request/',
         ElevatorSystemViewset.as_view({'post': 'request'}), name='request'),
     path('elevator-system/<int:system_id>/<int:pk>/request-data/',
         ElevatorViewset.as_view({'get': 'request_data'}), name='request-data'),
     path('elevator-system/<int:system_id>/<int:pk>/direction/',
         ElevatorViewset.as_view({'get': 'direction'}), name='direction'),
     path('elevator-system/<int:system_id>/<int:pk>/<int:mark>/isworking/',
         ElevatorViewset.as_view({'get': 'working'}), name='working'),   
     path('elevator-system/<int:system_id>/<int:pk>/<int:mark>/door/',
         ElevatorViewset.as_view({'get': 'door'}), name='door')                   

]