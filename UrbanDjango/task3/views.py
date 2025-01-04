from django.shortcuts import render


def platform_page(request):
    return render(request, "third_task\\platform.html")


def games_page(request):
    context = {
        "game_1": "Игра 1",
        "game_2": "Игра 2",
        "game_3": "Игра 2",
    }
    return render(request, "third_task\\games.html", context)


def cart_page(request):
    return render(request, "third_task\\cart.html")
