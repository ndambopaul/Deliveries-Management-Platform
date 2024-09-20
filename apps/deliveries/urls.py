from django.urls import path
from apps.deliveries.views import (
    deliveries,
    assign_rider,
    dispatch_delivery,
    complete_delivery,
    complete_deliveries,
    deliveries_pending_dispatch,
    deliveries_in_transit,
)

from apps.deliveries.bundled_deliveries.views import (
    new_bundle_delivery,
    bundle_deliveries,
    bundled_delivery_orders,
    add_order_to_bundled_delivery,
    complete_bundled_deliveries,
    bundled_deliveries_pending_dispatch,
    bundled_deliveries_in_transit
)

urlpatterns = [
    path("", deliveries, name="deliveries"),
    path("assign-rider/", assign_rider, name="assign-rider"),
    path("dispatch-delivery/", dispatch_delivery, name="dispatch-delivery"),
    path("complete-delivery/", complete_delivery, name="complete-delivery"),

    path("completed-deliveries/", complete_deliveries, name="completed-deliveries"),
    path("deliveries-in-transit/", deliveries_in_transit, name="deliveries-in-transit"),
    path("deliveries-pending-dispatch/", deliveries_pending_dispatch, name="deliveries-pending-dispatch"),

    path("bundle-deliveries/", bundle_deliveries, name="bundle-deliveries"),
    path("bundled-deliveries/<int:id>/orders/", bundled_delivery_orders, name="bundle-delivery-orders"),
    path("new-bundle-delivery/", new_bundle_delivery, name="new-bundle-delivery"),
    path("add-order-to-delivery/", add_order_to_bundled_delivery, name="add-order-to-delivery"),
    path("bundled-deliveries-completed/", complete_bundled_deliveries, name="bundled-deliveries-completed"),
    path("bundled-deliveries-pending-dispatch/", bundled_deliveries_pending_dispatch, name="bundled-deliveries-pending-dispatch"),
    path("bundled-deliveries-dispatched/", bundled_deliveries_in_transit, name="bundled-deliveries-dispatched"),
]
