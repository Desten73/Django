from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def main_page(request):
    return render(request, "index.html")


class Index2(TemplateView):
    template_name = "index.html"
