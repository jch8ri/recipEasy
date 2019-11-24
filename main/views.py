# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Recipes, Meals, Ingredients, Directions
# Create your views here.


def home(request):
    for i in Recipes:
        print(i.recipe_name)
