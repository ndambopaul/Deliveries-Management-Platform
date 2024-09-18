from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from apps.riders.models import Rider
from apps.users.models import User
from apps.deliveries.models import Delivery
# Create your views here.
@login_required(login_url="/users/login")
def riders(request):
    riders = Rider.objects.filter(tenant=request.tenant).order_by("-created")

    print(request.tenant)

    if request.method == "POST":
        search_text = request.POST.get("search_text")
        riders = Rider.objects.filter(Q(user__id_number__icontains=search_text)).filter(tenant=request.tenant).order_by("-created")

    
    paginator = Paginator(riders, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj
    }

    return render(request, "riders/riders.html", context)

@login_required(login_url="/users/login")
def new_rider(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        id_number = request.POST.get("id_number")
        phone_number = request.POST.get("phone_number")
        kra_pin = request.POST.get("kra_pin")
        gender = request.POST.get("gender")
        date_of_birth = request.POST.get("date_of_birth")
        address = request.POST.get("address")
        city = request.POST.get("city")
        country = request.POST.get("country")
        photo = request.FILES.get("photo")

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=id_number,
            email=email,
            id_number=id_number,
            kra_pin=kra_pin,
            phone_number=phone_number,
            role="RIDER",
            gender=gender,
            date_of_birth=date_of_birth,
            address=address,
            city=city,
            country=country,
            photo=photo,
            tenant=request.tenant
        )
        user.set_password("1234")
        user.save()

        Rider.objects.create(
            user=user,
            tenant=request.tenant
        )

        return redirect("riders")

    return render(request, "riders/new_rider.html")


def rider_deliveries(request, id):
    rider = Rider.objects.get(id=id)
    deliveries = Delivery.objects.filter(rider=rider, tenant=request.tenant)

    paginator = Paginator(deliveries, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "rider": rider
    }

    return render(request, "riders/rider_deliveries.html", context)