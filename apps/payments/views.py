from decimal import Decimal
from django.shortcuts import render, redirect
from django.db.models import Q
from django.db import transaction
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from apps.payments.models import (
    ClientInvoice,
    DeliveryPayments,
    RiderPayment,
    RiderEarning,
    RiderPayout,
)
from apps.riders.models import Rider


# Create your views here.
@login_required(login_url="/users/login")
def rider_earnings(request):
    earnings = RiderEarning.objects.filter(tenant=request.tenant)

    paginator = Paginator(earnings, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}
    return render(request, "payments/rider/earnings.html", context)


@login_required(login_url="/users/login")
def earning_payments(request, id):
    earning = RiderEarning.objects.get(id=id)
    rider_payments = RiderPayment.objects.filter(earning=earning).order_by("-created")

    paginator = Paginator(rider_payments, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}
    return render(request, "payments/rider/rider_payments.html", context)


@login_required(login_url="/users/login")
def rider_payments(request):
    rider_payments = RiderPayment.objects.filter(tenant=request.tenant).order_by(
        "-created"
    )

    paginator = Paginator(rider_payments, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}
    return render(request, "payments/rider/delivery_payments.html", context)


@login_required(login_url="/users/login")
def rider_payouts(request):
    rider_payouts = RiderPayout.objects.filter(tenant=request.tenant).order_by(
        "-created"
    )

    paginator = Paginator(rider_payouts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}
    return render(request, "payments/rider_payouts.html", context)


@login_required(login_url="/users/login")
def new_payout(request):
    if request.method == "POST":
        earning_id = request.POST.get("earning_id")
        amount = Decimal(request.POST.get("amount"))

        earning = RiderEarning.objects.get(id=earning_id)

        payout = RiderPayout.objects.create(
            tenant=request.tenant, earning=earning, rider=earning.rider, amount=amount
        )

        earning.balance -= amount
        earning.amount_paid += amount
        earning.save()

        payout.balance = earning.balance
        payout.save()

        return redirect("rider-payouts")
    return render(request, "payments/new_payout.html")
