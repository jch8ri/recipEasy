# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Meals, Recipes, Ingredients, Directions

# Register your models here.

admin.site.register(Meals)
admin.site.register(Recipes)
admin.site.register(Ingredients)
admin.site.register(Directions)
