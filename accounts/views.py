from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login

def registration_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return redirect("todo:list")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})
