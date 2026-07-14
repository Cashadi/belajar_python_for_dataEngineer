# # Your first print function
# print("Hello, world!")

# # Fill in the print function
# print("Welcome to the recipe scaler")

# # Store the pasta type as a string
# pasta_type = "spaghetti"

# # Store the quantity as an integer
# quantity = 80

# # Print the pasta type
# print(pasta_type)

# # Print the quantity
# print(quantity)

# # Update the pasta type to fusilli
# pasta_type = "fusilli"

# # Update the quantity to 100
# quantity = 100

# print(pasta_type)
# print(quantity)

# # Store the number of garlic cloves as an integer
# garlic_cloves = 3

# # Store the olive oil amount as a float
# olive_oil_tbsp = 2.5
# print(olive_oil_tbsp)

# # Increase the olive oil amount
# new_olive_oil_tbsp = olive_oil_tbsp + 1

# print(garlic_cloves)
# print(new_olive_oil_tbsp)

# # Track if you have pasta at home
# has_pasta = True

# # Track if you have garlic
# has_garlic = False

# print(has_pasta)
# print(has_garlic)

# # Check the data type of olive_oil_tbsp
# print(type(olive_oil_tbsp))

# # Check the data type of has_pasta
# print(type(has_pasta))

# # Store the multi-line cooking instructions
# # Step 1: Boil water in a large pot
# # Step 2: Add pasta and cook for 10 minutes
# # Step 3: Drain and serve with sauce
# cooking_instructions = """
# # Store the multi-line cooking instructions
# # Step 1: Boil water in a large pot
# # Step 2: Add pasta and cook for 10 minutes
# # Step 3: Drain and serve with sauce
# """

# print(cooking_instructions)

# # Original pasta type
# pasta_type = "pasta"

# # Update pasta type to be more specific
# pasta_type = pasta_type.replace("pasta", "fusilli pasta")

# ingredient_one = "BASIL"

# # Standardize ingredient_one to lowercase
# ingredient_one = ingredient_one.lower()

# print(pasta_type)
# print(ingredient_one)

# # Create a list of ingredients
# ingredients = ["fusilli", "tomatoes", "garlic", "basil", "olive oil", "salt"]

# # Create a list of ingredient quantities
# quantities = [500, 400, 15, 20, 30, 10]

# print(ingredients)
# print(quantities)

# ingredients = ["fusilli", "tomatoes", "garlic", "basil", "olive oil", "salt"]
# quantities = [500, 400, 15, 20, 30, 10]

# # Get the second ingredient for your preview
# second_ingredient = ingredients[1]

# # Get the last quantity using slice notation
# last_quantity = quantities[-1:]

# # Get every other ingredient, starting with the first
# alternate_ingredient = ingredients[::2]

# print(second_ingredient)
# print(last_quantity)
# print(alternate_ingredient)

# # Create the recipe dictionary
# recipe = {"olive_oil": 30, 
# # Add garlic
#           "garlic": 15,
# # Add tomatoes
#           "tomatoes": 400}

# print(recipe)

# # Create the recipe dictionary
# recipe = {"olive_oil": 30,
# # Add garlic
#           "garlic": 15,
# # Add tomatoes
#           "tomatoes": 400}

# # Add basil to the recipe dictionary
# recipe["basil"] = 20

# print(recipe)

# # Get all ingredient names
# ingredient_names = recipe.keys()

# # Get all quantities
# quantities = recipe.values()

# # Get all key-value pairs
# recipe_items = recipe.items()

# print("Ingredient names:", ingredient_names)
# print("Quantities:", quantities)
# print("Recipe items:", recipe_items)

# # Create a tuple
# cup_conversion = (1, 240)

# # Check the type
# print(type(cup_conversion))

# pantry_stock = {"tomatoes": 500}
# ingredients_needed = {"tomatoes": 400}

# # Check if you have enough tomatoes for the full party
# if pantry_stock["tomatoes"] >= ingredients_needed["tomatoes"]:
#     print("Enough tomatoes for the party!")

# # Check if you have enough for a smaller gathering
# elif pantry_stock["tomatoes"] >= 800:
#     print("Only enough tomatoes for a smaller gathering.")

# ingredients = ["fusilli", "tomatoes", "garlic", "basil", "olive oil", "salt"]

# # Loop through each ingredient in the list
# for item in ingredients:
#     print(item)
    
# Iterate over the number of ingredients
# for item in range(1, 7):
#     print("Adding ingredient", item)

# quantities = [500, 400, 20, 15, 15, 7]

# # Loop through each quantity in the recipe
# for qty in quantities:
#     # Check if it's a large quantity (400g or more)
#     if qty >= 400:
#         print('Large quantity')
#     # Check if it's a medium quantity (200g or more)
#     elif qty >= 200:
#         print('Medium quantity')
#     # Otherwise it's a small quantity
#     else:
#         print('Small quantity')

#         recipe = {
#     "fusilli": 500,
#     "tomatoes": 400,
#     "basil": 20,
#     "garlic": 15,
#     "olive oil": 15,
#     "salt": 7
# }

# # Loop through the recipe dictionary items
# for ingredient, qty in recipe.items():
#     # Calculate the scaled quantity by multiplying by 2
#     scaled_qty = qty * 2
    
#     print(ingredient, ":", scaled_qty, "g")

total_confirmations = 10
guest_count = 0

# Count confirmations using a while loop
while guest_count < total_confirmations:
    guest_count += 1
    print(guest_count, "guests so far!")

print("We have", guest_count, "guests coming!")

total_ingredients = 7
ingredients_checked = 0

# Set up the loop
while ingredients_checked < total_ingredients:
    # Increment the counter
    ingredients_checked += 1
    # Check if less than 4 ingredients reviewed
    if ingredients_checked < 4:
        print("More than half remaining")
    # Check if 6 or fewer ingredients reviewed
    elif ingredients_checked <= 6:
        print("Nearly finished checking")
    else:
        print("All ingredients verified!")