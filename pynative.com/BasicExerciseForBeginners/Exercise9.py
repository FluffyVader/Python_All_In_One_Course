# Exercise 9: Check Palindrome Number
# Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.

# Expected Output:

# original number 121
# Yes. given number is palindrome number

# original number 125
# No. given number is not palindrome number
def custom_str_reverse(str_to_reverse):
    result = ""

    for index in range (len(str_to_reverse)-1, -1, -1):
        result += str_to_reverse[index]

    return result


def is_panindromeV1(number):
    original_number_str = str(number)

    reversed_number = custom_str_reverse(original_number_str)

    if original_number_str == reversed_number:
        print(f"The original number is {original_number_str}")
        print("Yes, the given number is a panindrome number")

    else:
        print(f"The original number is {original_number_str}")
        print("No, the given number is not a panindrome number")

is_panindromeV1(1)

is_panindromeV1(121212)

is_panindromeV1(1000000000000000000000000110101)


def is_panindromeV2(number):
    original_number_str = str(number)

    reversed_str = original_number_str[::-1]

    if original_number_str == reversed_str:
        print(f"The original number is {original_number_str}")
        print("The number given is a Panindrome")

    else:
        print(f"The original number is {original_number_str}")
        print("The number given is not a Panindrome")

print("_-_-_-_-_-_-_-")

is_panindromeV2(1)

is_panindromeV2(121212)

is_panindromeV2(1000000000000000000000000110101)

