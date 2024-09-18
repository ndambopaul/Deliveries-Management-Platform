from django.urls import path
from apps.riders.views import riders, new_rider, rider_deliveries

urlpatterns = [
    path("", riders, name="riders"),
    path("new-rider/", new_rider, name="new-rider"),
    path("rider/<int:id>/deliveries/", rider_deliveries, name="rider-deliveries"),
]