from django.urls import path
from integrations.views import OrderAPICollectionAPIView

urlpatterns = [
    path("collect-order/", OrderAPICollectionAPIView.as_view(), name="collect-order"),
]