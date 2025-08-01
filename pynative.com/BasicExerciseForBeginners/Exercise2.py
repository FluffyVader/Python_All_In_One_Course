# Exercise 2: Print the Sum of a Current Number and a Previous number
# Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.

# Expected Output:

# Printing current and previous number sum in a range(10)
# Current Number 0 Previous Number  0  Sum:  0
# Current Number 1 Previous Number  0  Sum:  1
# Current Number 2 Previous Number  1  Sum:  3
# Current Number 3 Previous Number  2  Sum:  5
# Current Number 4 Previous Number  3  Sum:  7
# Current Number 5 Previous Number  4  Sum:  9
# Current Number 6 Previous Number  5  Sum:  11
# Current Number 7 Previous Number  6  Sum:  13
# Current Number 8 Previous Number  7  Sum:  15
# Current Number 9 Previous Number  8  Sum:  17

previousNumber = 0
for currentNumber in range(0, 10, 1):
    sum = currentNumber + previousNumber

    print(f"Current number: {currentNumber} previous number: {previousNumber} sum is: {sum}")

    previousNumber = currentNumber

# 1. currentNumber = 0
# Loop:
# 2. if currentNumber < 10:
    # 3. do body of the loop
    # 4. currentNumber += 1 and goto step #2.
# 5. else Exit

#C/C++
# for (int prev = 0, curr = 0, sum = 0; curr < 10; prev = curr, ++curr)
# {
#     sum = prev + curr;
#     printf("current number: %d previous number: %d sum is: %d\n", curr, prev, sum);
# }
