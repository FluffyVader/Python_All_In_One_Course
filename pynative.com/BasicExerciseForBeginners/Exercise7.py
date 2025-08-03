# Exercise 7: Find the number of occurrences of a substring in a string
# Write a Python code to find how often the substring “Emma” appears in the given string.

# Given:

# str_x = "Emma is good developer. Emma is a writer"
# Expected Output:

# Emma appeared 2 times


def count_subwords(text, word_to_find):

    answer = text.count(word_to_find)

    return answer

count = count_subwords("Emma is good developer. Emma is a writer", "Emma")
print(f"the word that has been selected to find has been found {count} times")

count = count_subwords("AAAAAAAAAA", "AAA")
print(f"the word that has been selected to find has been found {count} times")