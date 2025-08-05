# Exercise 14: Print a downward half-pyramid pattern of stars
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

def print_downward_pyramid(height):
    for i in range(0, height + 1, 1):
        for j in range(0, height-i, 1):
            print("*",  end = " " )
        print(" ")

print_downward_pyramid(5)
print_downward_pyramid(7)
print_downward_pyramid(1)
