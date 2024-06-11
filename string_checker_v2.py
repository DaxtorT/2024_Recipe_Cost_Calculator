# Tried a 'while' loop instead of 'if' statement
# Added the '- 1' because the 'len()' function starts from 1 whereas the 'valid_list[]' starts from 0

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
        error = f"Please choose from {valid_list}"

        # Ask user for choice (and force lowercase)
        response = input(question).lower()
        
        # Runs through list and if response is an item in list (or first letter the full name is returned)
        for item in valid_list:
            # If 'first_letter' is set to yes then check the list for first letter and full strings
            if num_letters > 0:
                if response == item[:num_letters] or response == item:
                    return item
            # If 'first_letter' is set to no then only check the list for full strings
            else:
                if response == item:
                    return item

        # Output error if response not in list        
        print(error)

# Lists
y_n_list = ["yes", "no"]
allowed_units = ["g", "kg", "mL", "L"]

# Main Routine goes here
test_yes_no = string_checker("Yes or No? ", y_n_list, 1)
print()
ingredient_name = input("Name of Ingredient: ")
ingredient_amount = input("Amount of Ingredient: ")
ingredient_unit = string_checker("Unit of Ingredient: ", allowed_units, 0)