from datetime import datetime
import calendar
from django.shortcuts import render, redirect
from django.db.models import Q
from django.db import transaction
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from apps.deliveries.models import Delivery, DeliveryStatusUpdate, DeliveryOrder
from apps.riders.models import Rider
from apps.clients.models import OrderStatusUpdate, Order
from apps.payments.models import RiderEarning, RiderPayment

date_today = datetime.now().date()


# Create your views here.
@login_required(login_url="/users/login")
def deliveries(request):
    deliveries = Delivery.objects.filter(tenant=request.tenant, delivery_type="Single Order").order_by("-created")
    paginator = Paginator(deliveries, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    riders = Rider.objects.filter(tenant=request.tenant).filter(busy=False)

    context = {"page_obj": page_obj, "riders": riders}

    return render(request, "deliveries/deliveries.html", context)


@login_required(login_url="/users/login")
@transaction.atomic
def complete_delivery(request):
    if request.method == "POST":
        delivery_id = request.POST.get("delivery_id")
        delivery = Delivery.objects.get(id=delivery_id)
        delivery.delivery_status = "Complete"
        delivery.save()

        delivery.rider.busy = False
        delivery.rider.save()

        DeliveryStatusUpdate.objects.create(
            delivery=delivery, previous_status="Dispatched", next_status="Completed"
        )

        if delivery.delivery_type == "Single Order":
            delivery.order.order_status = "Delivered"
            delivery.order.save()

            OrderStatusUpdate.objects.create(
                order=delivery.order, previous_status="Dispatched", next_status="Delivered"
            )
        elif delivery.delivery_type == "Multiple Orders":
            orders = delivery.deliveryorders.all()
            orders.update(delivery_status="Complete")

            for delivery_order in orders:
                delivery_order.order.order_status = "Delivered"
                delivery_order.order.save()

                OrderStatusUpdate.objects.create(
                    order=delivery_order.order, previous_status="Dispatched", next_status="Delivered"
                )

        ## Handle Rider Payment
        month_name = calendar.month_name[date_today.month]
        rider_earning = RiderEarning.objects.filter(
            rider=delivery.rider, month=month_name
        ).first()

        if rider_earning:
            rider_payment = RiderPayment.objects.create(
                earning=rider_earning,
                tenant=request.tenant,
                rider=delivery.rider,
                amount=delivery.delivery_cost,
                delivery=delivery,
            )

            rider_payment.earning.total_amount += rider_payment.amount
            rider_payment.earning.balance += rider_payment.amount
            rider_payment.earning.save()

        else:
            rider_earning = RiderEarning.objects.create(
                tenant=request.tenant,
                rider=delivery.rider,
                month=month_name,
                year=date_today.year,
            )

            rider_payment = RiderPayment.objects.create(
                earning=rider_earning,
                tenant=request.tenant,
                rider=delivery.rider,
                amount=delivery.delivery_cost,
                delivery=delivery,
            )

            rider_payment.earning.total_amount += rider_payment.amount
            rider_payment.earning.balance += rider_payment.amount
            rider_payment.earning.save()

        if delivery.delivery_type == "Single Order":
            return redirect("deliveries-in-transit")
        elif delivery.delivery_type == "Multiple Orders":
            return redirect("bundled-deliveries-dispatched")

    return render(request, "deliveries/mark_complete.html")


@login_required(login_url="/users/login")
def assign_rider(request):
    if request.method == "POST":
        delivery_id = request.POST.get("delivery_id")
        rider_id = request.POST.get("rider")

        rider = Rider.objects.get(id=rider_id)
        rider.save()

        delivery = Delivery.objects.get(id=delivery_id)
        delivery.rider = rider
        delivery.save()

        if delivery.delivery_type == "Single Order":
            return redirect("deliveries-pending-dispatch")
        elif delivery.delivery_type == "Multiple Orders":
            return redirect("bundled-deliveries-pending-dispatch")
        
    return render(request, "deliveries/assign_rider.html")


@login_required(login_url="/users/login")
@transaction.atomic
def dispatch_delivery(request):
    if request.method == "POST":
        delivery_id = request.POST.get("delivery_id")

        delivery = Delivery.objects.get(id=delivery_id)
        delivery.delivery_status = "In Transit"
        delivery.save()


        delivery.rider.busy = True
        delivery.rider.save()

        DeliveryStatusUpdate.objects.create(
            delivery=delivery,
            previous_status="Pending Dispatch",
            next_status="Dispatched",
        )

        if delivery.delivery_type == "Single Order":
            delivery.order.order_status = "Dispatched"
            delivery.order.save()

            OrderStatusUpdate.objects.create(
                order=delivery.order,
                previous_status="Set For Delivery",
                next_status="Dispatched",
            )
            return redirect("deliveries-pending-dispatch")

        elif delivery.delivery_type == "Multiple Orders":
            orders = delivery.deliveryorders.all()
            orders.update(delivery_status="Dispatched")

            for delivery_order in orders:
                delivery_order.order.order_status = "Dispatched"
                delivery_order.order.save()

                OrderStatusUpdate.objects.create(
                    order=delivery_order.order,
                    previous_status="Set For Delivery",
                    next_status="Dispatched"
                )
                return redirect("bundled-deliveries-pending-dispatch")

    return render(request, "deliveries/dispatch_delivery.html")


@login_required(login_url="/users/login")
def complete_deliveries(request):
    deliveries = Delivery.objects.filter(
        tenant=request.tenant, delivery_status="Complete", delivery_type="Single Order"
    ).order_by("-created")

    paginator = Paginator(deliveries, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}

    return render(request, "deliveries/complete_deliveries.html", context)


@login_required(login_url="/users/login")
def deliveries_pending_dispatch(request):
    deliveries = Delivery.objects.filter(
        tenant=request.tenant, delivery_status="Pending Dispatch", delivery_type="Single Order"
    ).order_by("rider")

    paginator = Paginator(deliveries, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    riders = Rider.objects.filter(tenant=request.tenant).filter(busy=False)

    context = {"page_obj": page_obj, "riders": riders}

    return render(request, "deliveries/deliveries_pending_dispatch.html", context)


@login_required(login_url="/users/login")
def deliveries_in_transit(request):
    deliveries = Delivery.objects.filter(
        tenant=request.tenant, delivery_status="In Transit", delivery_type="Single Order"
    ).order_by("-created")

    paginator = Paginator(deliveries, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}

    return render(request, "deliveries/deliveries_in_transit.html", context)

