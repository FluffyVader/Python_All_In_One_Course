# Exercise 21: Check if a user-entered string contains any digits using a for loop
# Expected Output:

# Enter a string: Pynative123Python
# The string contains at least one digit.

# Enter a string: PYnativeffff6
# The string does not contain any digits.

user_str = str(input("Please enter a string here: "))
number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def does_str_have_digit(str_to_use):
    for char in str_to_use:
        if char in number_list:
            print(f"Your input ({str_to_use}) has at least 1 digit")
            return True

    print(f"Your input ({str_to_use}) does not have any digits")
    return False



# if user_str.isdigit():
#     print(f"The user input ({user_str}) has digits")
# else:
#     print(f"The user input ({user_str}) does not have digits")

does_str_have_digit(user_str)
