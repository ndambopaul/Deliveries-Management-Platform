from django.urls import path
from apps.deliveries.views import (
    deliveries,
    assign_rider,
    dispatch_delivery,
    complete_delivery,
    complete_deliveries,
    deliveries_pending_dispatch,
    deliveries_in_transit
)

urlpatterns = [
    path("", deliveries, name="deliveries"),
    path("assign-rider/", assign_rider, name="assign-rider"),
    path("dispatch-delivery/", dispatch_delivery, name="dispatch-delivery"),
    path("complete-delivery/", complete_delivery, name="complete-delivery"),

    path("completed-deliveries/", complete_deliveries, name="completed-deliveries"),
    path("deliveries-in-transit/", deliveries_in_transit, name="deliveries-in-transit"),
    path("deliveries-pending-dispatch/", deliveries_pending_dispatch, name="deliveries-pending-dispatch"),
]
