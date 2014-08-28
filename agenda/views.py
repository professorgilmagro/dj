# -*- coding: utf8 -*-

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from forms import form_schedule_item
from models import schedule_item
from django.contrib.auth.decorators import login_required, permission_required


def index(request):
    return render(request, "index.html")


@permission_required("agenda.change.schedule_item")
def listing(request):
    params = request.GET

    if "q" in params and len(params["q"]) > 0:
        items = schedule_item.objects.filter(subject__icontains=params["q"])
        q = params["q"]
    else:
        items = schedule_item.objects.all()
        q = ""

    return render(request, "lista.html", {"items": items, "query": q})


@login_required
def create(request):
    if request.method == 'POST':
        form = form_schedule_item(request.POST, request.FILES)

        if form.is_valid():
            info = form.cleaned_data
            item = schedule_item(
                date=info['date'],
                time=info['time'],
                subject=info['subject'],
                description=info['description']
            )

            item.user = request.user
            item.save()

            # item.participants.add(item)
            return listing(request)
    else:
        form = form_schedule_item()

    return render(request, "adiciona.html", {'form': form})


@login_required
def edit(request, pk_value):
    item = get_object_or_404(schedule_item, pk=pk_value, user=request.user)

    if request.method == 'POST':
        form = form_schedule_item(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            return listing(request)

    else:
        form = form_schedule_item(instance=item)

    return render(request, "edita.html", {"form": form})


@login_required
def delete(request, pk_value):
    item = get_object_or_404(schedule_item, pk=pk_value)
    item.delete()
    return listing(request)
