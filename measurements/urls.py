from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_measurements, name='measurementList'),
    path('detail/<llave>/', views.get_measurementDetail, name='measurementDetail'),
    path('delete/<llave>/', views.delete_measurementDetail, name='deleteMeasurement'),
    path('modify/<llave>/opcion/<int:opcion>/variable/<variable>/', views.modify_measurementDetail, name='modifyMeasurement'),
    path('create/variable/<variable>/value/<value>/unit/<unit>/place/<place>', views.create_measurementDetail, name='createMeasurement')
]