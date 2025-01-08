from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import RegistrationForm


# Create your views here.
def registration_page(request):
    users = ["user", "qwerty", "qwer"]
    info = dict()

    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        email = request.POST.get("email")
        age = request.POST.get("age")
        agreement = request.POST.get("agreement") == "on"

        print(name, password, repeat_password, email, age, agreement)

        if password != repeat_password:
            info["error"] = "Пароли не совпадают!"
        if int(age) < 18:
            info["error"] = "Вы должны быть старше 18 лет!"
        if name in users:
            info["error"] = "Пользователь уже существует!"
        if password == repeat_password and int(age) > 17 and name not in users:
            info["info"] = f"Приветствуем, {name}!"

    return render(request, "fifth_task\\registration_page.html", info)


def registration_page_django(request):
    users = ["user", "qwerty", "qwer"]
    info = dict()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            email = form.cleaned_data["email"]
            age = form.cleaned_data["age"]
            agreement = form.cleaned_data["agreement"]
            if password != repeat_password:
                info["error"] = "Пароли не совпадают!"
            if int(age) < 18:
                info["error"] = "Вы должны быть старше 18 лет!"
            if name in users:
                info["error"] = "Пользователь уже существует!"
            if password == repeat_password and int(age) > 17 and name not in users:
                info["info"] = f"Приветствуем, {name}!"
    else:
        form = RegistrationForm()
    info["form"] = form
    return render(request, "fifth_task\\registration_page.html", info)


def test(request):
    name = request.GET.get("name", "user")
    age = request.GET.get("age", "18")
    return HttpResponse(f"Hello, {name} {age}!")
