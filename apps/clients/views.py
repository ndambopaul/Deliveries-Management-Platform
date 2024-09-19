from django.shortcuts import render

from django.shortcuts import render, redirect
from django.db.models import Q
from django.db import transaction
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from apps.clients.models import Client, Order, OrderStatusUpdate
from apps.deliveries.models import Delivery, DeliveryStatusUpdate
from apps.clients.methods.upload_orders import UploadOrdersMixin


# Create your views here.
@login_required(login_url="/users/login")
def clients(request):
    clients = Client.objects.filter(tenant=request.tenant).order_by("-created")

    paginator = Paginator(clients, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}
    return render(request, "clients/clients.html", context)


@login_required(login_url="/users/login")
def client_details(request, id):
    client = Client.objects.get(id=id)
    orders = client.clientorders.all().order_by("-created")

    paginator = Paginator(orders, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, "client": client}
    return render(request, "clients/client_details.html", context)


@login_required(login_url="/users/login")
def client_orders(request, id):
    client = Client.objects.get(id=id)
    orders = client.clientorders.all().order_by("-created")

    paginator = Paginator(orders, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, "client": client}

    return render(request, "orders/client_orders.html", context)


@login_required(login_url="/users/login")
def new_client(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        website = request.POST.get("website")
        address = request.POST.get("address")
        town = request.POST.get("town")
        country = request.POST.get("country")

        Client.objects.create(
            tenant=request.tenant,
            name=name,
            phone_number=phone_number,
            email=email,
            website=website,
            address=address,
            town=town,
            country=country,
        )
        return redirect("clients")
    return render(request, "clients/new_client.html")


@login_required(login_url="/users/login")
def edit_client(request):
    if request.method == "POST":
        client_id = request.POST.get("client_id")
        name = request.POST.get("name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        website = request.POST.get("website")
        address = request.POST.get("address")
        town = request.POST.get("town")
        country = request.POST.get("country")

        client = Client.objects.get(id=client_id)
        client.name = name
        client.phone_number = phone_number
        client.email = email
        client.website = website
        client.address = address
        client.town = town
        client.country = country
        client.save()

        return redirect("clients")
    return render(request, "clients/new_client.html")


@login_required(login_url="/users/login")
def delete_client(request):
    if request.method == "POST":
        client_id = request.POST.get("client_id")
        client = Client.objects.get(id=client_id)
        client.delete()
        return redirect("clients")
    return render(request, "clients/new_client.html")


## Orders Management
@login_required(login_url="/users/login")
def orders(request):
    orders = Order.objects.filter(tenant=request.tenant).order_by("-created")
    clients = Client.objects.filter(tenant=request.tenant).order_by("-created")

    paginator = Paginator(orders, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, "clients": clients}

    return render(request, "orders/orders.html", context)


@login_required(login_url="/users/login")
def new_order(request):
    if request.method == "POST":
        order_number = request.POST.get("order_number")
        customer_name = request.POST.get("customer_name")
        customer_phone = request.POST.get("customer_phone")
        customer_location = request.POST.get("customer_location")
        customer_address = request.POST.get("customer_address")
        delivery_cost = request.POST.get("delivery_cost")
        client_id = request.POST.get("client_id")

        order = Order.objects.create(
            tenant=request.tenant,
            order_number=order_number,
            customer_name=customer_name,
            customer_phone=customer_phone,
            customer_location=customer_location,
            customer_address=customer_address,
            client_id=client_id,
            delivery_cost=delivery_cost,
        )
        OrderStatusUpdate.objects.create(
            order=order, previous_status="Created", next_status="Pending Dispatch"
        )
        return redirect("orders")
    return render(request, "orders/new_order.html")


@login_required(login_url="/users/login")
@transaction.atomic
def dispatch_order(request):
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        order = Order.objects.get(id=order_id)
        order.order_status = "Set For Delivery"
        order.save()

        OrderStatusUpdate.objects.create(
            order=order,
            previous_status="Pending Dispatch",
            next_status="Set For Delivery",
        )

        delivery = Delivery.objects.create(
            order=order,
            tenant=request.tenant,
            delivery_status="Pending Dispatch",
            delivery_cost=order.delivery_cost,
        )

        DeliveryStatusUpdate.objects.create(
            delivery=delivery, previous_status="Created", next_status="Pending Dispatch"
        )
        return redirect("pending-dispatch-orders")
    return render(request, "orders/dispatch_order.html")


@login_required(login_url="/users/login")
def edit_order(request):
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        order_number = request.POST.get("order_number")
        customer_name = request.POST.get("customer_name")
        customer_phone = request.POST.get("customer_phone")
        customer_location = request.POST.get("customer_location")
        customer_address = request.POST.get("customer_address")
        delivery_cost = request.POST.get("delivery_cost")

        order = Order.objects.get(id=order_id)
        order.tenant = request.tenant
        order.order_number = order_number
        order.customer_name = customer_name
        order.customer_phone = customer_phone
        order.customer_location = customer_location
        order.customer_address = customer_address
        order.delivery_cost = delivery_cost
        order.save()

        return redirect("orders")
    return render(request, "orders/edit_order.html")


@login_required(login_url="/users/login")
def delete_order(request):
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        order = Order.objects.get(id=order_id)
        order.delete()

        return redirect("orders")
    return render(request, "orders/delete_order.html")


@login_required(login_url="/users/login")
def upload_orders(request):
    if request.method == "POST":
        orders_file = request.FILES.get("orders_file")
        client_id = request.POST.get("client_id")

        client = Client.objects.get(id=client_id)

        try:
            mixin = UploadOrdersMixin(file=orders_file, client=client)
            mixin.run()

        except Exception as e:
            raise e

        return redirect(f"/clients/client-orders/{client_id}")
    return render(request, "orders/upload_orders.html")
