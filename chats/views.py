from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from chats.models import Group


# Create your views here.

@login_required
def index(request):
    groups = Group.objects.all()
    return render(request, 'chats/home.html', {'groups': groups})


@login_required
def new_group(request):
    u = request.user
    new = Group.objects.create()
    new.members.add(u)
    new.save()
    return redirect('chats:index')


@login_required
def join_group(request, uuid):
    u = request.user
    groups = Group.objects.get(uuid=uuid)
    groups.members.add(u)
    groups.save()
    return redirect('chats:index')


@login_required
def leave_group(request, uuid):
    u = request.user
    groups = Group.objects.get(uuid=uuid)
    groups.members.remove(u)
    groups.save()
    return redirect('chats:index')


@login_required
def open_chat(request, uuid):
    groups = Group.objects.get(uuid=uuid)
    if request.user not in groups.members.all():
        return redirect('chats:index')
    messages = groups.message_set.all()
    sorted_messages = sorted(messages, key=lambda x: x.timestamp)
    return render(request, 'chats/paperchat.html', context={'messages': sorted_messages, 'uuid': uuid})


@login_required
def remove_group(request, uuid):
    u = request.user
    Group.objects.get(uuid=uuid).delete()
    return redirect('chats:index')
