# Fixed data for unit conversion
ingre_names = ["Cheese", "Flour", "Milk", "Caviar", "Eggs"]
ingre_amounts = [100, 250, 200, 10, 2]
ingre_units = ["g", "g", "mL", "tbsp", "item"]

bought_amounts = [500, 1.5, 2, 350, 12]
bought_units = ["g", "kg", "L", "mL", "item"]
bought_costs = [8.60, 1.9, 3.80, 50, 8.5]

# Conversions Data
unit_conversions = {
    "kg":1000,
    "L":1000,
    "tsp":4.92,
    "tbsp":14.78
}

required_factors = []

bought_factors = []

# Converting required ingredient units
print("*** Converting Required Ingredients ***")
for item in ingre_units:
    if item in unit_conversions:
        print("Converting Unit...")
        conversion_factor = unit_conversions[item]
        if item == "kg":
            print(f"Unit was converted from '{item}' to 'g'.")
        else:
            print(f"Unit was converted from '{item}' to 'mL'.")

    else:
        print("Unit already converted")
        conversion_factor = "equal"
        
    required_factors.append(conversion_factor)
    print(conversion_factor)
    print()

# Converting bought ingredient units
print("*** Converting Bought Ingredients ***")
for item in bought_units:
    if item in unit_conversions:
        print("Converting Unit...")
        conversion_factor = unit_conversions[item]
        if item == "kg":
            print(f"Unit was converted from '{item}' to 'g'.")
        else:
            print(f"Unit was converted from '{item}' to 'mL'.")

    else:
        print("Unit already converted")
        conversion_factor = "equal"
    
    bought_factors.append(conversion_factor)
    print(conversion_factor)
    print()

# Print Results of conversions
print("*** Convertions of Required Ingredients ***")
print(required_factors)
print()

print("*** Convertions of Bought Ingredients ***")
print(bought_factors)
print()

print("ALL Ingredients Converted!!")