# Recipe Size Converter

This Python script helps chefs convert the sizes of recipes based on the desired number of servings. By adjusting ingredient quantities proportionally, it allows you to scale recipes up or down easily.

## Features

- Convert recipe ingredient quantities based on new serving sizes.
- Simple and easy-to-use function.
- Modular code that can be easily integrated into other projects.

## Usage

### Function

The main function, `convert_recipe`, takes three parameters:
- `recipe`: A dictionary where keys are ingredient names and values are their quantities.
- `original_servings`: The number of servings the original recipe makes.
- `new_servings`: The number of servings desired.

It returns a dictionary with the adjusted ingredient quantities.

### Example

Here is an example of how to use the script:

```python
def convert_recipe(recipe, original_servings, new_servings):
    """
    Convert the recipe ingredients to match the new desired serving size.

    Parameters:
    recipe (dict): Dictionary where keys are ingredient names and values are quantities.
    original_servings (int): The number of servings the original recipe makes.
    new_servings (int): The number of servings desired.

    Returns:
    dict: A dictionary with the adjusted ingredient quantities.
    """
    conversion_factor = new_servings / original_servings
    converted_recipe = {ingredient: quantity * conversion_factor for ingredient, quantity in recipe.items()}
    return converted_recipe

if __name__ == "__main__":
    # Example usage
    original_recipe = {
        "flour (cups)": 2,
        "sugar (cups)": 1,
        "eggs": 2,
        "milk (cups)": 1.5,
        "butter (cups)": 0.5
    }

    original_servings = 4
    new_servings = 8

    adjusted_recipe = convert_recipe(original_recipe, original_servings, new_servings)

    print(f"Original Recipe for {original_servings} servings:")
    for ingredient, quantity in original_recipe.items():
        print(f"{ingredient}: {quantity}")

    print(f"\nAdjusted Recipe for {new_servings} servings:")
    for ingredient, quantity in adjusted_recipe.items():
        print(f"{ingredient}: {quantity:.2f}")
```
```
Output
Running the script with the provided example will yield:

Original Recipe for 4 servings:
flour (cups): 2
sugar (cups): 1
eggs: 2
milk (cups): 1.5
butter (cups): 0.5

Adjusted Recipe for 8 servings:
flour (cups): 4.00
sugar (cups): 2.00
eggs: 4.00
milk (cups): 3.00
butter (cups): 1.00
```

## Installation
To run this script, ensure you have Python installed on your system. Clone this repository and run the script using a Python interpreter.

```sh
git clone https://github.com/CireWire/fuzzy-octo-train.git
cd fuzzy-octo-train
python convert_recipe.py
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
