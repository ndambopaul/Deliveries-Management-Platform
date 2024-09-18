from django.urls import path
from apps.users.views import user_login, user_logout, register_user, employees, new_employee, edit_employee, delete_employee

urlpatterns = [
    path("login/", user_login, name="login"),
    path("register/", register_user, name="register"),
    path("logout/", user_logout, name="logout"),

    # Employees
    path("employees/", employees, name="employees"),
    path("new-employee/", new_employee, name="new-employee"),
    path("edit-employee/", edit_employee, name="edit-employee"),
    path("delete-employee/", delete_employee, name="delete-employee"),
]