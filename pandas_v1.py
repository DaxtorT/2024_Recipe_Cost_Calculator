import pandas

# Functions go here
# Function for adding currency formatting
def currency(x):
    return f"${x:.2f}" 

# Set up dicts and lists
ingre_names = ["Cheese", "Flour", "Milk", "Caviar", "Eggs", "Sugar"]
ingre_amounts = [100, 250, 200, 10, 2, 1.5]
ingre_units = ["g", "g", "mL", "tbsp", "item", "cup"]

bought_amounts = [500, 1.5, 2, 350, 12, 500]
bought_units = ["g", "kg", "L", "mL", "item", "ml"]
bought_costs = [8.60, 1.9, 3.80, 50, 8.5, 2]

ingredient_costs = [1.72, 0.3166, 0.38, 21.1142, 1.4166, 1.44]

recipe_cost_dict = {
    "Ingredient Name": ingre_names ,
    "Needed Amount": ingre_amounts,
    "Needed Unit": ingre_units,
    "Bought Amount": bought_amounts,
    "Bought Unit": bought_units,
    "Bought Cost": bought_costs,
    "Ingredient Cost": ingredient_costs
}

# Main Routine goes here
recipe_name = input("Recipe Name: ")
recipe_servings = int(input(f"How many servings of {recipe_name}: "))

# Make the pandas frame from dictionary of information
recipe_cost_frame = pandas.DataFrame(recipe_cost_dict)

# Find total of all ingredients
total_ingre_cost = recipe_cost_frame['Ingredient Cost'].sum()

# Calculate cost per serving of recipe
print(type(total_ingre_cost))
print(type(recipe_servings))
per_serving = total_ingre_cost / recipe_servings

# Currency Formatting (Uses currency function)
add_dollars = ['Bought Cost', 'Ingredient Cost']
for item in add_dollars:
    recipe_cost_frame[item] = recipe_cost_frame[item].apply(currency)

# Print The Frame
print("---- Ingredient Costs ----")
print(recipe_cost_frame.to_string(index=False))
print(f"Total Ingredient Costs: ${total_ingre_cost:.2f}")
print(f"Cost Per Serving: ${per_serving:.2f}")