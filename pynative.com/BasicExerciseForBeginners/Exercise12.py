# Exercise 12: Calculate income tax
# Calculate income tax for the given income by adhering to the rules below

# Taxable Income	Rate (in %)
# First $10,000	0
# Next $10,000	10
# The remaining	20
# Expected Output:

# For example, suppose the income is 45000, and the income tax payable is

#10000*0% + 10000*10%  + 25000*20% = $6000

#9000 -> 0
#19000 -> 10000 * 0 + 9000 * 0.1 = 900
#25000 -> 10000 * 0 + 10000 * 0.1 + 5000 * 0.2 = 1000+1000 ==2000


def calculate_income_tax(income):
    first_taxable_amount = 10000
    second_taxable_amount = 10000
    tax_to_pay = 0

    if income <= 10000:
        tax_to_pay = 0
        return tax_to_pay
    
    elif income > 10000 and income < 20000:
        tax_to_pay = (first_taxable_amount * 0.0) + (income - first_taxable_amount) * 0.1
        return tax_to_pay

    else:
        tax_to_pay = (first_taxable_amount * 0.0) + (second_taxable_amount * 0.1) + (income - first_taxable_amount - second_taxable_amount) * 0.2
        return tax_to_pay

############################################################################################    

salary = 9000
print(f"salary: {salary} the tax amount you have to pay pay is: {calculate_income_tax(salary)}")
salary = 10000
print(f"salary: {salary} the tax amount you have to pay pay is: {calculate_income_tax(salary)}")
salary = 19000
print(f"salary: {salary} the tax amount you have to pay pay is: {calculate_income_tax(salary)}")
salary = 20000
print(f"salary: {salary} the tax amount you have to pay pay is: {calculate_income_tax(salary)}")
salary = 45000
print(f"salary: {salary} the tax amount you have to pay pay is: {calculate_income_tax(salary)}")