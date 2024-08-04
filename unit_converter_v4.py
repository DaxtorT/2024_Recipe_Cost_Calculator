# Fixed data for unit conversion
ingre_names = ["Cheese", "Flour", "Milk", "Caviar", "Eggs", "Sugar"]
ingre_amounts_input = [100, 250, 200, 10, 2, 1.5]
ingre_units_input = ["g", "g", "mL", "tbsp", "item", "cup"]

bought_amounts_input = [500, 1.5, 2, 350, 12, 500]
bought_units_input = ["g", "kg", "L", "mL", "item", "ml"]
bought_costs = [8.60, 1.9, 3.80, 50, 8.5, 2]

ingre_units = []
ingre_amounts = []
ingre_factors = []
bought_units = []
bought_amounts = []
bought_factors = []

# Conversions Data
unit_conversions = {
    "kg":1000,
    "L":1000,
    "tsp":4.92,
    "tbsp":14.78,
    "cup":240
}

# Functions go here
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
        ingre_amounts.append(conversion_out)
        ingre_factors.append(conversion_factor)
        ingre_units.append(converted_to)
    else:
        bought_amounts.append(conversion_out)
        bought_factors.append(conversion_factor)
        bought_units.append(converted_to)

# Main Routine goes here
loop_iterate = 0
for unit in ingre_units_input:
    unit_converter(unit, ingre_amounts_input[loop_iterate], "required")
    loop_iterate += 1

loop_iterate = 0
for unit in bought_units_input:
    unit_converter(unit, bought_amounts_input[loop_iterate], "bought")
    loop_iterate += 1   

# Print Results of conversions
print("Required Stuff")
print(ingre_units_input)
print()
print(ingre_units)
print()
print()
print("Bought Stuff")
print(bought_units_input)
print()
print(bought_units)
print()

loop_iterate = 0

print("Fancy Stuff")
for item in ingre_names:
    print(f"{item}: Original Values: {ingre_amounts_input[loop_iterate]}{ingre_units_input[loop_iterate]} \n    Uniform Values: {ingre_amounts_input[loop_iterate]}*{ingre_factors[loop_iterate]}={ingre_amounts[loop_iterate]} {ingre_units[loop_iterate]}")
    loop_iterate += 1


print("ALL Ingredients Converted!!")