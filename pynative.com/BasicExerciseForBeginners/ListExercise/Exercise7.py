# Exercise 7: Count Occurrences
# Count and print how many times 'Football' appears in list.

# Given:

# sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis'].

############################################################################
def str_counter(given_list, word_to_find):
    word_counter = 0
    for word in given_list:
        if word == word_to_find:
            word_counter += 1
    
    return word_counter

############################################################################

sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis']
counter2 = sports.count("Football")
print(f"The word Football has appeared {counter2} times")

print(f"The word Football has appeared {str_counter(sports, "Football")} times")