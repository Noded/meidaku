from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required
def paperchat(request):
    return render(request, 'paper/chat.html', {})


def room(request, room_name):
    return render(request, 'paper/room.html',{
        'room_name': room_name
    },)
