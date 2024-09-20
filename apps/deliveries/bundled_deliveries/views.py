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



# Bundle Deliveries
def bundle_deliveries(request):
    deliveries = Delivery.objects.filter(tenant=request.tenant, delivery_type="Multiple Orders").order_by("-created")
    paginator = Paginator(deliveries, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    riders = Rider.objects.filter(tenant=request.tenant).filter(busy=False)

    context = {"page_obj": page_obj, "riders": riders}

    return render(request, "deliveries/bundled_deliveries/bundle_deliveries.html", context)


def bundled_delivery_orders(request, id):
    delivery = Delivery.objects.get(id=id)

    orders = DeliveryOrder.objects.filter(delivery=delivery)

    context = {
        "delivery": delivery,
        "orders": orders
    }

    return render(request, "deliveries/bundled_deliveries/delivery_orders.html", context)

def new_bundle_delivery(request):
    if request.method == "POST":
        delivery_type = "Multiple Orders"
        delivery_status = "Pending Dispatch"

        delivery = Delivery.objects.create(
            tenant=request.tenant,
            delivery_type=delivery_type,
            delivery_status=delivery_status,
        )
        DeliveryStatusUpdate.objects.create(
            delivery=delivery,
            previous_status="Created",
            next_status="Pending Dispatch"
        )
        return redirect("bundle-deliveries")
    return render(request, "deliveries/bundled_deliveries/new_delivery.html")

@login_required(login_url="/users/login")
@transaction.atomic
def add_order_to_bundled_delivery(request):
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        delivery_id = request.POST.get("delivery_id")

        delivery = Delivery.objects.get(id=delivery_id)
        order = Order.objects.get(id=order_id)

        OrderStatusUpdate.objects.create(
            order=order,
            previous_status="Pending Dispatch",
            next_status="Set For Delivery"
        )

        delivery.delivery_cost += order.delivery_cost
        delivery.save()

        order.order_status="Set For Delivery"
        order.save()

        DeliveryOrder.objects.create(
            tenant=request.tenant,
            order=order,
            delivery=delivery,
            rider=delivery.rider if delivery.rider else None,
            delivery_status="Pending Dispatch",
            delivery_cost=order.delivery_cost
        )
        
        return redirect("pending-dispatch-orders")
    return render(request, "deliveries/bundled_deliveries/add_order_to_delivery.html")


@login_required(login_url="/users/login")
def complete_bundled_deliveries(request):
    deliveries = Delivery.objects.filter(
        tenant=request.tenant, delivery_status="Complete", delivery_type="Multiple Orders"
    ).order_by("-created")

    paginator = Paginator(deliveries, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}

    return render(request, "deliveries/bundled_deliveries/complete_deliveries.html", context)


@login_required(login_url="/users/login")
def bundled_deliveries_pending_dispatch(request):
    deliveries = Delivery.objects.filter(
        tenant=request.tenant, delivery_status="Pending Dispatch", delivery_type="Multiple Orders"
    ).order_by("rider")

    paginator = Paginator(deliveries, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    riders = Rider.objects.filter(tenant=request.tenant).filter(busy=False)

    context = {"page_obj": page_obj, "riders": riders}

    return render(request, "deliveries/bundled_deliveries/deliveries_pending_dispatch.html", context)


@login_required(login_url="/users/login")
def bundled_deliveries_in_transit(request):
    deliveries = Delivery.objects.filter(
        tenant=request.tenant, delivery_status="In Transit", delivery_type="Multiple Orders"
    ).order_by("-created")

    paginator = Paginator(deliveries, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}

    return render(request, "deliveries/bundled_deliveries/deliveries_in_transit.html", context)
