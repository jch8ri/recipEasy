# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Meals(models.Model):
    meal_type = models.CharField(max_length=100)
    meal_summary = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Meals'

    def __str__(self):
        return self.meal_type


class Recipes(models.Model):
    recipe_name = models.CharField(max_length=100)
    meals = models.ManyToManyField(Meals)

    def __str__(self):
        return self.recipe_name


class Ingredients(models.Model):
    ingredient_name = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient_name


class Directions(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    directions = models.TextField()

    def __str__(self):
        return self.directions
