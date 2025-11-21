from django.urls import path
from .views import huespedleercrear, huespedeliminarmodificar

urlpatterns = [
    path('huesped/',huespedleercrear.as_view(), name='huesped-list-create'),
    path('huesped/<int:pk>/',huespedeliminarmodificar.as_view(), name='huesped-detail-update-delete'),
]
