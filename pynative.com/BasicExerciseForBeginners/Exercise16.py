# Exercise 18: Check if a given year is a leap year
# A leap year is a year in the Gregorian calendar that contains an extra day, making it 366 days long instead of the usual 365. This extra day, 
# February 29th, is added to keep the calendar synchronized with the Earth’s revolution around the Sun.

# Generally, a year is a leap year if it is divisible by 4. 
# However, there's an exception: if the year is divisible by 100, it's not a leap year unless it's also divisible by 400. 

#############################################################################

def leap_year_or_not(year):
    is_leap = False

    if year % 4 == 0:
        is_leap = True
        
        if year % 100 == 0:
            is_leap = False
            
            if year % 400 == 0:
                is_leap = True

    if is_leap == True:
        print(f"The given year({year}) is a leap year")
    else:
        print(f"The given year({year}) is not a leap year")

#############################################################################

leap_year_or_not(2000)
leap_year_or_not(1900)
leap_year_or_not(2028)
leap_year_or_not(1)
leap_year_or_not(28)
leap_year_or_not(678)


