# Fixed data for unit conversion
ingre_names = ["Cheese", "Flour", "Milk", "Caviar"]
ingre_amounts = [100, 250, 200, 10]
ingre_units = ["g", "g", "mL", "g"]

bought_amounts = [500, 1.5, 2, 350]
bought_units = ["g", "kg", "L", "mL"]
bought_costs = [8.60, 1.9, 3.80, 50]

# Converion Data
conversion_data = []

# Math to convert units
unit_iterate = 0
for item in ingre_units:
    if item == bought_units[unit_iterate]:
        result = 1

    elif item == "g":
        if bought_units[unit_iterate] == "kg":
            result = 0.001
        else:
            result = "error"
    
    elif item == "kg":
        if bought_units[unit_iterate] == "g":
            result = 1000
        else:
            result = "error"

    elif item == "mL":
        if bought_units[unit_iterate] == "L":
            result = 0.001
        else:
            result = "error"

    elif item == "L":
        if bought_units[unit_iterate] == "mL":
            result = 1000
        else:
            result = "error"

    else:
        result = "error"

    unit_iterate += 1
    conversion_data.append(result)

# Print process of each ingredient conversion
print_iterate = 0
for item in conversion_data:
    if item == "error":
        print(f"There was an error with the conversion of {ingre_names[print_iterate]}.")

    else:
        unit_converted = ingre_amounts[print_iterate] * item
        print(f"The unit conversion for {ingre_names[print_iterate]} ({ingre_amounts[print_iterate]}{ingre_units[print_iterate]} of  {bought_amounts[print_iterate]}{bought_units[print_iterate]}), is {ingre_amounts[print_iterate]}{ingre_units[print_iterate]} * {item} = {unit_converted}{bought_units[print_iterate]}")

    print_iterate += 1

print()
print("ALL Ingredients Converted!!")