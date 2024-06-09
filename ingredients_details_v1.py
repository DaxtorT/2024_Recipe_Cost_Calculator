# Lists
ingre_names = []
ingre_amounts = []
ingre_units = []

bought_amounts = []
bought_units = []
bought_costs = []

# Variables

# Get Required Ingredient Info
while True:
    ingredient_name = input("Name of Ingredient: ")
    if ingredient_name == "xxx":
        print()
        break
    ingredient_amount = float(input("Amount of Ingredient: "))
    ingredient_unit = input("Unit of Ingredient: ")

    ingre_names.append(ingredient_name)
    ingre_amounts.append(ingredient_amount)
    ingre_units.append(ingredient_unit)
    
    print()

# Get Bought Ingredient Info
bought_num = 0
for item in ingre_names:
    buy_amount = float(input(f"How much of {ingre_names[bought_num]} have you bought? "))
    buy_unit = input(f"What unit is {ingre_names[bought_num]} measured in? ")
    buy_cost = float(input(f"How much did you buy {ingre_names[bought_num]} for? $"))
                
    bought_amounts.append(buy_amount)
    bought_units.append(buy_unit)
    bought_costs.append(buy_cost)

    print()
    bought_num += 1

# Test print statement
iterate_num = 0
for item in ingre_names:
    # Math to figure out cost of each ingredient
    cost_ingredient = ingre_amounts[iterate_num] / bought_amounts[iterate_num] * bought_costs[iterate_num]

    # Print results of that math
    print(f"You need {ingre_amounts[iterate_num]}{ingre_units[iterate_num]} of {ingre_names[iterate_num]}. You have bought {bought_amounts[iterate_num]}{bought_units[iterate_num]} of {ingre_names[iterate_num]} for ${bought_costs[iterate_num]}. The amount of {ingre_names[iterate_num]} you need will cost ${cost_ingredient}")
    iterate_num += 1