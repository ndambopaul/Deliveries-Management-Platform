from django.urls import path
from apps.deliveries.views import deliveries, assign_rider, dispatch_delivery, complete_delivery

urlpatterns = [
    path("", deliveries, name="deliveries"),
    path("assign-rider/", assign_rider, name="assign-rider"),
    path("dispatch-delivery/", dispatch_delivery, name="dispatch-delivery"),
    path("complete-delivery/", complete_delivery, name="complete-delivery"),
]