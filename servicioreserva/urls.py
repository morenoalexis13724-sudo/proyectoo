from django.urls import path
from .views import servicioreservaleercrear, servicioreservaeliminarmodificar

urlpatterns = [
    path('servicioreserva/',servicioreservaleercrear.as_view(), name='servicioreserva-list-create'),
    path('servicioreserva/<int:pk>/',servicioreservaeliminarmodificar.as_view(), name='servicioreserva-detail-update-delete'),
]