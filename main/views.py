from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    """
    Класс для отображения главной страницы сайта meidaku
    """
    template_name = "main/index.html"

# def index(request):
#     return render(request, 'main/index.html')
