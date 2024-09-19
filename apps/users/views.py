from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from apps.users.models import User


# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session["cashier_id"] = user.id

            login(request, user)
            return redirect("home")
    return render(request, "accounts/login.html")


@login_required(login_url="/users/login/")
def user_logout(request):
    logout(request)
    return redirect("home")


def register_user(request):
    return render(request, "accounts/register.html")


@login_required(login_url="/users/login")
def employees(request):
    user = request.user
    employees = User.objects.all().order_by("-created")
    if not user.is_superuser:
        employees = (
            User.objects.filter(tenant=request.tenant)
            .filter(role__in=["ADMIN", "EMPLOYEE"])
            .order_by("-created")
        )

    paginator = Paginator(employees, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}

    return render(request, "employees/employees.html", context)


@login_required(login_url="/users/login")
def new_employee(request):
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
        role = request.POST.get("role")
        position = request.POST.get("position")

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=id_number,
            email=email,
            id_number=id_number,
            kra_pin=kra_pin,
            phone_number=phone_number,
            role=role,
            position=position,
            gender=gender,
            date_of_birth=date_of_birth,
            address=address,
            city=city,
            country=country,
            photo=photo,
            tenant=request.tenant,
        )
        user.set_password("1234")
        user.save()

        return redirect("employees")
    return render(request, "employees/new_employee.html")


@login_required(login_url="/users/login")
def edit_employee(request):
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
        role = request.POST.get("role")
        position = request.POST.get("position")
        employee_id = request.POST.get("employee_id")

        user = User.objects.get(id=employee_id)
        user.first_name = first_name if first_name else user.first_name
        user.last_name = last_name if last_name else user.last_name
        user.username = id_number if id_number else user.id_number
        user.email = email if email else user.email
        user.id_number = id_number if id_number else user.id_number
        user.kra_pin = kra_pin if kra_pin else user.kra_pin
        user.phone_number = phone_number if phone_number else user.phone_number
        user.role = role if role else user.role
        user.position = position if position else user.position
        user.gender = gender if gender else user.gender
        user.date_of_birth = date_of_birth if date_of_birth else user.date_of_birth
        user.address = address if address else user.address
        user.city = city if city else user.city
        user.country = country if country else user.country
        user.photo = photo if photo else user.photo
        user.save()

        return redirect("employees")
    return render(request, "employees/edit_employee.html")


@login_required(login_url="/users/login")
def delete_employee(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee_id")
        user = User.objects.get(id=employee_id)
        user.delete()
        return redirect("employees")
    return render(request, "employees/delete_employee.html")
