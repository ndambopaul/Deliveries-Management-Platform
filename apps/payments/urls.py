from django.urls import path
from apps.payments.views import rider_earnings, rider_payments, earning_payments, rider_payouts, new_payout

urlpatterns = [
    path("rider-earnings/", rider_earnings, name="rider-earnings"),
    path("earning/<int:id>/payments/", earning_payments, name="earning-payments"),
    path("rider-payments/", rider_payments, name="rider-payments"),
    path("rider-payouts/", rider_payouts, name="rider-payouts"),
    path("new-payout/", new_payout, name="new-payout"),
]