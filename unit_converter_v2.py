# Fixed data for unit conversion
ingre_names = ["Cheese", "Flour", "Milk", "Caviar"]
ingre_amounts = [100, 250, 200, 10]
ingre_units = ["g", "g", "mL", "g"]

bought_amounts = [500, 1.5, 2, 350]
bought_units = ["g", "kg", "L", "mL"]
bought_costs = [8.60, 1.9, 3.80, 50]

# Conversions Data
unit_conversions = {
    "g+kg":0.001,
    "kg+g":1000,
    "mL+L":0.001,
    "L+mL":1000
}

unit_factor = []

# Math to convert units
unit_iterate = 0

for item in ingre_units:
    if item == bought_units[unit_iterate]:
        conversion_factor = 1
        print("EQUAL")
        print()
        unit_factor.append(conversion_factor)
        unit_iterate += 1
        continue

    list_check = item + "+" + bought_units[unit_iterate]
    list_check = str(list_check)

    print(list_check)

    if list_check in unit_conversions:
        conversion_factor = unit_conversions[list_check]
        print("UNIT CHECKED")

    else:
        conversion_factor = "error"
        print("Unit Conversion was not possible")

    unit_factor.append(conversion_factor)

    unit_iterate += 1

    print()

print(f"Unit_Factor List: {unit_factor}\n")


# Print process of each ingredient conversion
print_iterate = 0
for item in unit_factor:
    if item == "error":
        print(f"There was an error with the conversion of {ingre_names[print_iterate]}.")

    else:
        unit_converted = ingre_amounts[print_iterate] * item
        print(f"The unit conversion for {ingre_names[print_iterate]} ({ingre_amounts[print_iterate]}{ingre_units[print_iterate]} of {bought_amounts[print_iterate]}{bought_units[print_iterate]}), is {ingre_amounts[print_iterate]}{ingre_units[print_iterate]} * {item} = {unit_converted}{bought_units[print_iterate]}")

    print_iterate += 1

print()
print("ALL Ingredients Converted!!")