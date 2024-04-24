from django.urls import path
from .views import orderItemView

urlpatterns = [
    path("orderitem/", orderItemView, name='orderitem'),
]