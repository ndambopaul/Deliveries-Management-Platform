from django.shortcuts import render

from django.shortcuts import render, redirect
from django.db.models import Q
from django.db import transaction
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from apps.clients.models import Client, Order, OrderStatusUpdate
from apps.deliveries.models import Delivery, DeliveryStatusUpdate, DeliveryOrder
from apps.clients.methods.upload_orders import UploadOrdersMixin


@login_required(login_url="/users/login")
def orders_pending_dispatch(request):
    orders = Order.objects.filter(
        tenant=request.tenant, order_status="Pending Dispatch"
    ).order_by("-created")
    clients = Client.objects.filter(tenant=request.tenant).order_by("-created")

    deliveries = Delivery.objects.filter(tenant=request.tenant, delivery_type="Multiple Orders", active=True)

    paginator = Paginator(orders, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "deliveries": deliveries
    }

    return render(request, "orders/orders_peding_dispatch.html", context)


@login_required(login_url="/users/login")
def orders_set_for_delivery(request):
    orders = Order.objects.filter(
        tenant=request.tenant, order_status="Set For Delivery"
    ).order_by("-created")

    paginator = Paginator(orders, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }

    return render(request, "orders/orders_set_for_delivery.html", context)


@login_required(login_url="/users/login")
def orders_delivered(request):
    orders = Order.objects.filter(
        tenant=request.tenant, order_status="Delivered"
    ).order_by("-created")

    paginator = Paginator(orders, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }

    return render(request, "orders/orders_delivered.html", context)
