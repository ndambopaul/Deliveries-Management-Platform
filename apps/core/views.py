from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/users/login")
def home(request):
    current_user = f"""
        username: {request.user.username},
        is_superuser: {request.user.is_superuser}
        email: {request.user.email}
        id: {request.user.id}
    """
    print(current_user)
    return render(request, "home.html")