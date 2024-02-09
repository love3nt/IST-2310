#  Write a python program that prompts the user for the number of items purchased and
# state. The program calculates appropriate discount based on quantity purchased and
# corresponding sales tax based on state. 

# All items are sold for $1, quantity must be greater than zero items, and only sold in CA, AZ, NV

# Sales Tax Rules:
# CA = 20%
# AZ = 10%
# NV = 5%

# Discount Rules:
# 10 or more items = 5% discount
# 20 or more items = 10% discount



# Prompt the user to input the # of items purchased.

items_purchased = int(input('\nPlease the number of items you purchased: '))

# Prompt the user to input the State in which they purchased the items.

state_purchased = input('\nPlease enter a valid state (CA, AZ, NV): ')

# Error check for anything entered other then a valid state.



