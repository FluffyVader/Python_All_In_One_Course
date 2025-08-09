# Exercise 22: Capitalize the first letter of each word in a string
# Expected Output:

# str1 = "pynative.com is for python lovers"
# Output Pynative.com Is For Python Lovers
####################################################################
str_to_capitalize = "pynative.com is for python lovers"

for first_symbol in str_to_capitalize:
    str_to_capitalize = str_to_capitalize.title()

print(str_to_capitalize)
####################################################################
#split str, capitalize every word (makes the first letter capital in each word), then print it

str_to_capitalize_tokens = str_to_capitalize.split()
capitalized_str = ""

for index, item in enumerate(str_to_capitalize_tokens):
    capitalized_item = item.capitalize()

    capitalized_str += capitalized_item
    if index != (len(str_to_capitalize_tokens) - 1):
        capitalized_str += " "

#capitalized_str = capitalized_str.strip()

print("-_-_-_-_-_-_")
print(capitalized_str)
#print(len(str_to_capitalize))
#print(len(capitalized_str))