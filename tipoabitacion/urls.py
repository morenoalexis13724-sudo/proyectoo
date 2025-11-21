from django.urls import path
from .views import tipohabitacionleercrear, tipohabitacioneliminarmodificar

urlpatterns = [
    path('tipohabitacion/',tipohabitacionleercrear.as_view(), name='tipohabitacion-list-create'),
    path('tipohabitacion/<int:pk>/',tipohabitacioneliminarmodificar.as_view(), name='tipohabitacion-detail-update-delete'),
]