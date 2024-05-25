import uuid

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404

from chats.forms import Join_To_Group
from chats.models import Group


# Create your views here.

@login_required
def index(request):
    if request.method == 'POST':
        form = Join_To_Group(request.POST)
        if form.is_valid():
            uuid = form.cleaned_data['uuid']
            group = get_object_or_404(Group, uuid=uuid)
            group.members.add(request.user)
            group.save()
    else:
        form = Join_To_Group()
    user = request.user
    groups = Group.objects.filter(members=user)
    return render(request, 'chats/home(new).html', {'groups': groups, 'user': user, 'form': form})


@login_required
def new_group(request):
    u = request.user
    new = Group.objects.create()
    new.members.add(u)
    new.save()
    return redirect('chats:index')


@login_required
def leave_group(request, uuid=None):
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
