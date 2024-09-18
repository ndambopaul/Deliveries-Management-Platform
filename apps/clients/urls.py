from django.urls import path
from apps.clients.views import clients, client_details, client_orders, new_client, edit_client, delete_client, orders, new_order, edit_order, delete_order, dispatch_order, upload_orders

urlpatterns = [
    path("", clients, name="clients"),
    path("<int:id>/details/", client_details, name="client-details"),
    path("client-orders/<int:id>/", client_orders, name="client-orders"),
    path("new-client/", new_client, name="new-client"),
    path("edit-client/", edit_client, name="edit-client"),
    path("delete-client/", delete_client, name="delete-client"),

    path("orders/", orders, name="orders"),
    path("new-order/", new_order, name="new-order"),
    path("edit-order/", edit_order, name="edit-order"),
    path("delete-order/", delete_order, name="delete-order"),
    path("dispatch-order/", dispatch_order, name="dispatch-order"),
    path("upload-orders/", upload_orders, name="upload-orders"),
]