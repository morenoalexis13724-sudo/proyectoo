from django.urls import path
from .views import clienteleercrear, clienteeliminarmodificar

urlpatterns = [
    path('cliente/',clienteleercrear.as_view(), name='cliente-list-create'),
    path('cliente/<int:pk>/',clienteeliminarmodificar.as_view(), name='cliente-detail-update-delete'),
]
