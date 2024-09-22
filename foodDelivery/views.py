from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.serializers import serialize

import json
from .models import *


def index(request):

    search = request.POST.get("search")
    if search:
        meals = Meal.objects.filter(name__icontains=search)

    else:
        meals = Meal.objects.all()

    context = {
        "meals": meals

    }

    return render(request, "index.html", context)


def getMeal(request, id):
    meal = Meal.objects.get(id=id)
    # data = serialize("json", Meal, fields=('name', 'price'))

    # ser = serializers.serialize("json", meals)
    # data = JsonResponse([meal.serialize() for meal in meals], safe=False)
    # print(json.loads(data.de))
    context = {
        "meal": meal
    }
    return render(request, "modal.html", context)
