from django.urls import path
from .views import habitacionleercrear, habitacioneliminarmodificar

urlpatterns = [
    path('habitacion/',habitacionleercrear.as_view(), name='habitacion-list-create'),
    path('habitacion/<int:pk>/',habitacioneliminarmodificar.as_view(), name='habitacion-detail-update-delete'),
]