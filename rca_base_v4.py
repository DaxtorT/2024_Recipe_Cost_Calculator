import pandas
import os.path

# Functions go here
# Function to check whether string is valid
def string_checker(question, valid_list, num_letters):
    while True:      
        # Error message generation
        error_length = len(valid_list)
        error_text = valid_list[0]

        while error_length > 1:
            error_text = error_text + f", {valid_list[error_length - 1]}"
            error_length -= 1

        # Print the customized error message
        error = f"Please choose from: {error_text}"

        # Ask user for choice (and force lowercase)
        response = input(question).lower()
        
        # Runs through list and if response is an item in list (or first letter the full name is returned)
        for item in valid_list:
            item = item.lower()
            # If 'first_letter' is set to yes then check the list for first letter and full strings
            if num_letters > 0:
                if response == item[:num_letters] or response == item:
                    return item
            # If 'first_letter' is set to no then only check the list for full strings
            elif num_letters == 0:
                if response == item:
                    return item

        # Output error if response not in list        
        print(error)

# Function to check whether number is a valid float or integer
def num_checker(question, error , float_int, zero):
    while True:
        try:
            response = float_int(input(question))
            
            if response <= 0:
                if zero == False:
                    print(error)
                else:
                    check = string_checker(f"Are you sure you mean $0? ", y_n_list, 1)
                    if check == "yes":
                        return response
                    else:
                        print(error)

            else:
                return response

        except ValueError:
            print(error)

# Function for checking string is not blank
def not_blank(question, error):
    while True:
        response = input(question)

        if response == "":
            print(error)
            continue
        
        return response

# Function for checking if a float can be a integer
def is_integer_float(x):
    return x == int(x)

# Function for converting units to one set usable unit E.g. kg to g
def unit_converter(unit, amount, req_buy):
    if unit in unit_conversions:
        conversion_factor = unit_conversions[unit]
        if unit == "kg":
            converted_to = "g"
        else:
            converted_to = "mL"
    else:
        conversion_factor = 1
        converted_to = unit

    if conversion_factor == 1:
        conversion_out = amount
    else:
        conversion_out = amount * conversion_factor

    check = is_integer_float(conversion_out)

    if check == False:
        conversion_out = '%.2f' % conversion_out

    if req_buy == "required":
        ingre_amounts_fix.append(conversion_out)
        ingre_factors_fix.append(conversion_factor)
        ingre_units_fix.append(converted_to)
    else:
        bought_amounts_fix.append(conversion_out)
        bought_factors_fix.append(conversion_factor)
        bought_units_fix.append(converted_to)

# Function for printing instructions
def instructions_display():
    print()
    print("--- Recipe Cost Calculator Instructions ---")
    print("The first thing you need to do is enter the name of your recipe. (Only used for naming things not too important)")
    print("You also need to enter the number of servings your recipe makes. (Whole numbers ONLY)")
    print()
    print("Next enter the name, amount of (unit), and the unit, of each ingredient you require for your recipe.")
    print("When you are done entering your ingredients type 'xxx' to tell the program you are done.")
    print("NOTE: This is different to what you have bought.")
    print()
    print("The last step is to enter the amount of (unit), the unit, and the cost of each ingredient that you bought.")
    print("NOTE: The name is done automatically as is goes through each ingredient you entered previously getting info.")
    print()
    print("Once you are done entering information it will create a text file under the name of the recipe you entered,")
    print("This will contain all the information about the costs.")
    print()

# Function for adding currency formatting to input
def currency(x):
    return f"${x:.2f}" 

# Lists
y_n_list = ["yes", "no"]
all_units = ["g", "kg", "mL", "L", "cup", "tsp", "tbsp", "item"]
g_units = ["g", "kg"]
ml_units = ["mL", "L", "cup", "tsp", "tbsp"]
item_units = ["item"]

ingre_names = []
ingre_amounts = []
ingre_units = []

bought_amounts = []
bought_units = []
bought_costs = []

ingre_units_fix = []
ingre_amounts_fix = []
ingre_factors_fix = []

bought_units_fix = []
bought_amounts_fix = []
bought_factors_fix = []

ingredient_costs = []

# Conversions Data
unit_conversions = {
    "kg":1000,
    "l":1000,
    "tsp":4.92,
    "tbsp":14.78,
    "cup":240
}

# Main Routine goes here
# Start information
print("*** WELCOME TO THE RECIPE COST CALCULATOR ***\n")
used_before = string_checker("Have you used the Recipe Cost Calculator before? ", y_n_list, 1)
if used_before == "no":
    instructions_display()
else:
    print()

# Get recipe info
print("--- Basic Recipe Information ---")
recipe_name = not_blank("Name of Recipe: ", "Please enter the name of your Recipe.")
recipe_servings = num_checker("How many servings does your recipe make? ", "Please enter a whole number.", int, False)
print()

# Get Required Ingredient Info
print(f"--- Needed Ingredient Information for {recipe_name} ---")
while True:
    ingredient_name = not_blank("Name of Ingredient: ", "Please enter the name of an Ingredient.")
    if ingredient_name == "xxx":
        print()
        break
    ingredient_amount = num_checker("Amount of Ingredient: ", "Please enter a positive number (Decimals are allowed).", float, False)
    ingredient_unit = string_checker("Unit of Ingredient: ", all_units, 0)

    ingre_names.append(ingredient_name)
    ingre_amounts.append(ingredient_amount)
    ingre_units.append(ingredient_unit)
    
    print()

# Get Bought Ingredient Info
print(f"--- Bought Ingredient Information for {recipe_name} ---")
bought_num = 0
for item in ingre_names:
    buy_amount = num_checker(f"How much '{ingre_names[bought_num]}' have you bought? ", "Please enter a positive number (Decimals are allowed)", float, False)
    if ingre_units[bought_num] == "kg" or ingre_units[bought_num] == "g":
        buy_unit_list = g_units
    elif ingre_units[bought_num] == "item":
        buy_unit_list = item_units
    else:
        buy_unit_list = ml_units
    buy_unit = string_checker(f"What unit is '{ingre_names[bought_num]}' measured in? ", buy_unit_list, 0)
    buy_cost = num_checker(f"How much did you buy '{ingre_names[bought_num]}' for? $", "Please enter a positive number (Decimals are allowed)", float, True)
                
    bought_amounts.append(buy_amount)
    bought_units.append(buy_unit)
    bought_costs.append(buy_cost)

    print()
    bought_num += 1

# Run each unit through the unit_converter
# Convert required ingredients
loop_iterate = 0
for unit in ingre_units:
    unit_converter(unit, ingre_amounts[loop_iterate], "required")
    loop_iterate += 1

# Convert bought ingredients
loop_iterate = 0
for unit in bought_units:
    unit_converter(unit, bought_amounts[loop_iterate], "bought")
    loop_iterate += 1  

# Calculate the cost of the ingredients
iterate_num = 0
for item in ingre_names:
    # Math to figure out cost of each ingredient
    cost_ingredient = float(ingre_amounts_fix[iterate_num]) / float(bought_amounts_fix[iterate_num]) * float(bought_costs[iterate_num])
    ingredient_costs.append(cost_ingredient)

# Calculate the cost per serving of the recipe
cost_length = len(ingredient_costs)
total_ingre_cost = ingredient_costs[0]


while cost_length > 1:
    total_ingre_cost += ingredient_costs[cost_length - 1]
    cost_length -= 1

# Calc cost per serving for recipe
per_serving = total_ingre_cost / recipe_servings


# Dictionary containing name of columns and lists for table
recipe_cost_dict = {
    "Ingredient Name": ingre_names ,
    "Needed Amount": ingre_amounts,
    "Needed Unit": ingre_units,
    "Bought Amount": bought_amounts,
    "Bought Unit": bought_units,
    "Bought Cost": bought_costs,
    "Ingredient Cost": ingredient_costs
}

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
recipe_text = f"-- {recipe_name} --"
recipe_cost_text = "-- Ingredient Cost Table --\n" + recipe_cost_table
total_text = "Total Ingredient Cost:\n" + f"${total_ingre_cost:.2f}"
serving_text = "Servings:\n" + f"{recipe_servings}"
per_serve_text = "Cost Per Serving:\n" + f"${per_serving:.2f}"

# List to iterate through for printing
to_write = [recipe_text, recipe_cost_text, total_text, serving_text, per_serve_text]

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