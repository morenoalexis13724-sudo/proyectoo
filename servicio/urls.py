from django.urls import path
from .views import servicioleercrear, servicioeliminarmodificar

urlpatterns = [
    path('servicio/',servicioleercrear.as_view(), name='servicio-list-create'),
    path('servicio/<int:pk>/',servicioeliminarmodificar.as_view(), name='servicio-detail-update-delete'),
]