import pandas
import os.path

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
print()

# Make the Pandas DataFrame from dictionary of information
recipe_cost_frame = pandas.DataFrame(recipe_cost_dict)

# Find total of all ingredients
total_ingre_cost = recipe_cost_frame['Ingredient Cost'].sum()

# Calculate cost per serving of recipe
per_serving = total_ingre_cost / recipe_servings

# Currency Formatting (Uses currency function)
add_dollars = ['Bought Cost', 'Ingredient Cost']
for item in add_dollars:
    recipe_cost_frame[item] = recipe_cost_frame[item].apply(currency)

# Create string from the DataFrame (so it can be written)
recipe_cost_table = recipe_cost_frame.to_string(index=False)

# Make all pieces of the written file variables for ease of printing
recipe_cost_text = "-- Ingredient Cost Table --\n" + recipe_cost_table
total_text = "Total Ingredient Cost:\n" + f"${total_ingre_cost:.2f}"
serving_text = "Servings:\n" + f"{recipe_servings}"
per_serve_text = "Cost Per Serving:\n" + f"${per_serving:.2f}"

# List to iterate through for printing
to_write = [recipe_name, recipe_cost_text, total_text, serving_text, per_serve_text]

# Create file to hold data (add .txt extension)
save_path = r'C:\Users\scrap\OneDrive - Massey High School\Year 12 (2024)\TCCOM2\Recipe Cost Assessment\Written Files'
file_name = f"{recipe_name}.txt"
complete_name = os.path.join(save_path, file_name)

# Print the complete path
print(f"Complete Path: {complete_name}\n")

# Writing to file
text_file = open(complete_name, "w+")
for item in to_write:
    text_file.write(item)
    text_file.write("\n\n")  

# Close the text file
text_file.close()

# Printing output
for item in to_write:
    print(item)
    print()