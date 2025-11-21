from django.urls import path
from .views import reservaleercrear, reservaeliminarmodificar

urlpatterns = [
    path('reserva/',reservaleercrear.as_view(), name='reserva-list-create'),
    path('reserva/<int:pk>/',reservaeliminarmodificar.as_view(), name='reserva-detail-update-delete'),
]