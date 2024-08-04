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
        error = f"Please choose from {error_text}."

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
def num_checker(question, error , float_int):
    while True:
        try:
            response = float_int(input(question))
            
            if response <= 0:
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

def is_integer_float(x):
    return x == int(x)

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

# Lists
y_n_list = ["yes", "no"]
allowed_units = ["g", "kg", "mL", "L", "cup", "tsp", "tbsp"]

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

# Conversions Data
unit_conversions = {
    "kg":1000,
    "l":1000,
    "tsp":4.92,
    "tbsp":14.78,
    "cup":240
}

# Main Routine goes here
# Get Required Ingredient Info
while True:
    ingredient_name = not_blank("Name of Ingredient: ", "Please enter the name of an Ingredient.")
    if ingredient_name == "xxx":
        print()
        break
    ingredient_amount = num_checker("Amount of Ingredient: ", "Please enter a positive number (Decimals are allowed).", float)
    ingredient_unit = string_checker("Unit of Ingredient: ", allowed_units, 0)

    ingre_names.append(ingredient_name)
    ingre_amounts.append(ingredient_amount)
    ingre_units.append(ingredient_unit)
    
    print()

# Get Bought Ingredient Info
bought_num = 0
for item in ingre_names:
    buy_amount = num_checker(f"How much '{ingre_names[bought_num]}' have you bought? ", "Please enter a positive number (Decimals are allowed)", float)
    buy_unit = string_checker(f"What unit is '{ingre_names[bought_num]}' measured in? ", allowed_units, 0)
    buy_cost = num_checker(f"How much did you buy '{ingre_names[bought_num]}' for? $", "Please enter a positive number (Decimals are allowed)", float)
                
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
print("Calculating Ingredient Cost")
iterate_num = 0
for item in ingre_names:
    # Math to figure out cost of each ingredient
    cost_ingredient = ingre_amounts_fix[iterate_num] / bought_amounts_fix[iterate_num] * bought_costs[iterate_num]
    cost_ingredient = '%.2f' % cost_ingredient

    # Print results of that math
    print(f"You need {ingre_amounts[iterate_num]}{ingre_units[iterate_num]} of {ingre_names[iterate_num]}. You have bought {bought_amounts[iterate_num]}{bought_units[iterate_num]} of {ingre_names[iterate_num]} for ${bought_costs[iterate_num]}. The amount of {ingre_names[iterate_num]} you need will cost ${cost_ingredient}")
    iterate_num += 1

print()
print("ALL Ingredients Converted!!")