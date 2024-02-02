# A customer in a store is purchasing five items. 
# Write a program that asks for the price of each item, 
# then displays the subtotal of the sale, 
# the amount of sales tax, and the total. 
# Assume the sales tax is 7 percent.

# Input statements 

item1 = float(input('Enter the price of item 1: '))
item2 = float(input('Enter the price of item 2: '))
item3 = float(input('Enter the price of item 3: '))
item4 = float(input('Enter the price of item 4: '))
item5 = float(input('Enter the price of item 5: '))

# calculate the total of all 5 items

items_total = (item1 + item2 + item3 + item4 + item5) 

# create a variable to specify the sales tax

sales_tax = 0.07

# calculate the subtotal 

subtotal = (items_total * sales_tax)

print(f'\n Your total after tax is: {subtotal:,.2f}')






