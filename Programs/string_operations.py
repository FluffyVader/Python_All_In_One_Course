# str1 = "abc" [::-1]

# print(str1)

def _reverse_(to_reverse):
    return to_reverse[::-1]

#####################################################################

def custom_str_reverse(str_to_reverse):
    result = ""

    for index in range (len(str_to_reverse)-1, -1, -1):
        result += str_to_reverse[index]

    return result

#####################################################################

def has_digits(string_to_test):
    #digits = ['0', '1', '2', '3', '4', '5','6','7','8', '9']
    
    for character in string_to_test:
        #if character in digits:
        if character.isdigit():
            return True

    return False

#####################################################################

def has_alpha(string_to_test):

    for char in string_to_test:
        if char.isalpha():
            return True

    return False
#####################################################################

str1 = _reverse_("this needs to be reversed")

reversed_string = custom_str_reverse(str1)

print(f"reversed_string: {reversed_string}")


string_to_test1 = "qwerty"
assert has_digits(string_to_test1) == False

string_to_test2 = "qwerty1"
assert has_digits(string_to_test2) == True

string_to_test3 = "12345"
assert has_alpha(string_to_test3) == False

string_to_test4 = "12345b"
assert has_alpha(string_to_test4) == True

