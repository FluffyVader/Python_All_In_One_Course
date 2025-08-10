# Exercise: 19: Print Alternate Prime Numbers till 20
# A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11).

# For example:

# All prime numbers from 1 to 20: 2, 3, 5, 7, 11, 13, 17, 19

# Alternate prime numbers from 1 to 20:
# 2, 5, 11, 17
# Refer:

# Python Programs to Check Prime Number
# Python Programs to Print alternate Prime Numbers

def isPrime(number):
    if number < 2:
        #print("This number is not prime")
        return False
    
    if number == 2:
        #print("This number is prime")
        return True
    
    if number % 2 == 0:
        #print('%d has factor %d' %(number, 2))
        #print("This number is not prime")
        return False

    trialUpperbound = number // 2
    trialFactor = 3

    # for i in range(2, 20, 3):
    #     print(isPrime([i]))


    while trialFactor <= trialUpperbound:
        if number % trialFactor == 0:
            #print('%d has factor %d' %(number, trialFactor))
            #print("This number is not prime")
            return False
        
        trialFactor += 2
    else:
        #print("This number is prime")
        return True

primary_number_counter = 0
prime_number_list = []
print("All prime numbers are: ", end = " ")
for i in range(0, 20 + 1, 1):
    if isPrime(i):
        prime_number_list.append(i)
        #primary_number_counter += 1
        #if primary_number_counter % 2 != 0:
        print(i, end =" ")


print("")
print("Allterate prime numbers are: ", end = "")
for index, prime_number in enumerate(prime_number_list):
    if index % 2 == 0:
        print(prime_number, end = " ")

# print("")
# print("Allterate prime numbers are: ", end = "")
# for index in range(0, len(prime_number_list) - 1, 2):
#     #if index % 2 == 0:
#     print(prime_number_list[index], end = " ")

