from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


@login_required
def paperchat(request):
    return render(request, 'main/paperchat.html')
