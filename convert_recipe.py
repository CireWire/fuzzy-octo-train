#!/usr/bin/env python

__author__ = "CireWire"

def convert_recipe(recipe, original_servings, new_servings):
    """
    Convert the recipe ingredients to match the new desired serving size.

    Parameters:
    recipe (dict): Dictionary
    where keys are ingredient names and values are quantities.
    
    original_servings (int): The number of servings the original recipe makes.

    new_servings (int): The number of servings desired.

    Returns:
    dict: A dictionary with the adjusted ingredient quantities.
    """

    conversion_factor = new_servings / original_servings

    converted_recipe = {ingredient: quantity * conversion_factor for ingredient, quantity in recipe.items()}
    
    return converted_recipe

# Example usage
original_recipe = {
    "flour (cups)" : 2,
    "sugar (cups)" : 1,
    "eggs" : 2,
    "milk (cups)" : 1.5,
    "butter (cups)" : 0.5
}

original_servings = 4
new_servings = 8

adjusted_recipe = convert_recipe(original_recipe, original_servings, new_servings)

print(f"\nOriginal Recipe for {original_servings} servings:")
for ingredient, quantity in original_recipe in original_recipe.items():
    print(f"{ingredient} : {quantity}")

print(f"\nAdjusted Recipe for {new_servings} servings: ")
for ingredient, quantity in adjusted_recipe.items():
    print(f"{ingredient}: {quantity:.2f}")
