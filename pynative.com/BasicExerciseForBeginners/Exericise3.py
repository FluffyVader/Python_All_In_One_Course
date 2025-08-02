# Exercise 3: Print characters present at an even index number
# Write a Python code to accept a string from the user and display characters present at an even index number.

# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

# Expected Output:

# Orginal String is  PYnative
# Printing only even index chars
# P
# n
# t
# v

####################################################################################

def print_even_characters_v1(str_to_print):

    print(f"Original String is {str_to_print}")
    print("Printing only even index chars")

    for index in range(0, len(str_to_print), 1):
        remainder = index % 2

        if remainder == 0:             #if remainder is 0 then index numer is even
            print(str_to_print[index])

    print(" ")
    
####################################################################################

def print_even_characters_v2(str_to_print):

    print(f"Original String is {str_to_print}")
    print("Printing only even index chars")

    for index in range(0, len(str_to_print), 2):
        print(str_to_print[index])

    print(" ")

####################################################################################

str_to_print = str(input("please enter the string: "))

print_even_characters_v1(str_to_print)
print_even_characters_v2(str_to_print)
