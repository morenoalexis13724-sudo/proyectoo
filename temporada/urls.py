from django.urls import path
from .views import temporadaleercrear, temporadaeliminarmodificar

urlpatterns = [
    path('temporada/',temporadaleercrear.as_view(), name='temporada-list-create'),
    path('temporada/<int:pk>/',temporadaeliminarmodificar.as_view(), name='temporada-detail-update-delete'),
]