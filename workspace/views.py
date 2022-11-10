from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from workspace.models import Dish, DishType, Ingredient


@login_required
def index(request):
    """View function for the home page of the site."""

    num_cooks = get_user_model().objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()
    num_ingredients = Ingredient.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
        "num_ingredients": num_ingredients,
        "num_visits": num_visits + 1,
    }

    return render(request, "workspace/index.html", context=context)
