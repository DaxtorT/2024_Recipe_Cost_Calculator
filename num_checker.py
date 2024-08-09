def num_checker(question, error , float_int, zero):
    while True:
        try:
            response = float_int(input(question))
            
            if response <= 0:
                if zero == False:
                    print(error)
                else:
                    check = input(f"Are you sure you mean $0? ")
                    if check == "yes":
                        return response
                    else:
                        print(error)

            else:
                return response

        except ValueError:
            print(error)

# Main Routine goes here
servings = num_checker("Please enter the number of Servings: ", "Please enter a whole number above zero (No decimals)", int, False)
print()
ingre_amount = num_checker("Please enter the amount of Ingredient: ", "Please enter a number above zero", float, False)