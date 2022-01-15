from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def main(request):
    return render(request, "users/main.html")


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return render(request, "users/success.html")

            return render(request, "users/login.html")

        ctx = {"form": form}
        return render(request, "users/login.html", ctx)


def log_out(request):
    logout(request)
    return redirect("users:main")
