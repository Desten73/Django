from django.shortcuts import render


def platform_page(request):
    return render(request, "fourth_task\\platform.html")


def games_page(request):
    list_games = ["Игра 1", "Игра 2", "Игра 3"]
    context = {
        "list_games": list_games,
    }
    return render(request, "fourth_task\\games.html", context)


def cart_page(request):
    return render(request, "fourth_task\\cart.html")
