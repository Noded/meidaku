import uuid

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from chats.forms import Join_To_Group, Create_Group
from chats.models import Group


# Create your views here.


@login_required
def index(request):
    join_form = Join_To_Group()
    create_form = Create_Group()

    if request.method == "POST":
        action = request.POST.get("action")
        
        # Обработка формы присоединения к группе
        if action == "join":
            join_form = Join_To_Group(request.POST)
            if join_form.is_valid():
                uuid = join_form.cleaned_data["uuid"]
                try:
                    group = Group.objects.get(uuid=uuid)
                    if request.user in group.members.all():
                        messages.warning(request, "Вы уже состоите в этой группе")
                    else:
                        group.members.add(request.user)
                        group.save()
                        messages.success(request, f"Вы успешно присоединились к группе {group.name}")
                        return redirect("chats:index")
                except ObjectDoesNotExist:
                    messages.error(request, "Группа с таким UUID не найдена")
        
        # Обработка формы создания новой группы
        elif action == "create":
            create_form = Create_Group(request.POST)
            if create_form.is_valid():
                name = create_form.cleaned_data["name"]
                new_group = Group.objects.create(name=name)
                new_group.members.add(request.user)
                new_group.save()
                messages.success(request, f"Группа '{name}' успешно создана")
                return redirect("chats:index")

    user = request.user
    groups = Group.objects.filter(members=user)
    return render(
        request,
        "chats/home_paperchat.html",
        {"groups": groups, "user": user, "join_form": join_form, "create_form": create_form},
    )

@login_required
def new_group(request):
    """Create_new_group

    Args:
        request get: get

    Returns:
        Create a group: Create group and return to index(main page)
    """
    u = request.user
    new = Group.objects.create()
    new.members.add(u)
    new.save()
    return redirect("chats:index")


@login_required
def leave_group(request, uuid=None):
    """Leave from chat group

    Args:
        request get: get

    Returns:
        Create a group: Create group and return to index(main page)
    """
    u = request.user
    groups = Group.objects.get(uuid=uuid)
    groups.members.remove(u)
    groups.save()
    return redirect("chats:index")


@login_required
def open_chat(request, uuid):
    """Open chat group

    Args:
        request: get

    Returns:
        Returns to chat page
    """
    groups = Group.objects.get(uuid=uuid)
    if request.user not in groups.members.all():
        return redirect("chats:index")
    if request.method == "POST":
        form = Join_To_Group(request.POST)
        if form.is_valid():
            uuid = form.cleaned_data["uuid"]
            try:
                group = Group.objects.get(uuid=uuid)

                # Проверяем, не состоит ли уже пользователь в группе
                if request.user in group.members.all():
                    messages.warning(request, "Вы уже состоите в этой группе")

                group.members.add(request.user)
                group.save()
                messages.success(
                    request, f"Вы успешно присоединились к группе"
                )

            except ObjectDoesNotExist:
                messages.error(request, "Группа с таким UUID не найдена")
    else:
        form = Join_To_Group()
    messages = groups.message_set.all()
    sorted_messages = sorted(messages, key=lambda x: x.timestamp)

    user = request.user
    groups = Group.objects.filter(members=user)
    return render(
        request,
        "chats/paperchat.html",
        context={
            "messages": sorted_messages,
            "uuid": uuid,
            "groups": groups,
            "user": user,
            "form": form,
        },
    )


@login_required
def remove_group(request, uuid):
    """Delete chat group

    Args:
        request get: get
        uuid (str): id of group for del in db

    Returns:
        Nothing: returns nothing cause chat deleting
    """
    u = request.user
    Group.objects.get(uuid=uuid).delete()
    return redirect("chats:index")
