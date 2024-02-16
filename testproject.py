import time 
import os 

# Project 1

# The Dollar Store: A store sells all items for $1. The store has the following rules

# Discount Rules:
# Customers buying 10 or more items receive a 5% discoun
# Customers buying 20 or more items receive a 10% discount

# State Tax Rules:
# CA = 20%
# AZ = 10%
# NV = 5%

# Other Rules:
# Quantity must be greater than zero
# Valid states are CA, AZ, and NV

# Task: Write a python program that prompts the user for the number of items purchased and
# 	state. The program calculates appropriate discount based on quantity purchased and
# 	corresponding sales tax based on state




#############################################
###         TIMED WELCOME MESSAGE         ###
#############################################


def greeting_message(message, n):
    print(message)
    time.sleep(n)
    os.system('cls' if os.name == 'nt' else 'clear')

message = '\nWelcome!\n \nThis program calculates appropriate discount based on quantity purchased and corresponding sales tax based on state'
n = 5          
greeting_message(message, n)


#############################################
###         DECLARING FUNCTIONS           ###
#############################################


# This will calculate the state tax based on what state was entered.
def calculate_state_tax(valid_state):
    if valid_state == 'CA':
        return 0.20
    elif valid_state == 'AZ':
        return 0.10
    elif valid_state == 'NV':
        return 0.05
    else:
        return None

# This will calculate the discount to be applied based on the quantity of items entered.
def calculate_discount(item_quantity):
    if item_quantity >= 20:
        return 0.10
    elif item_quantity >= 10:
        return 0.05
    else:
        return 0


#############################################
###           MAIN PROGRAM LOOP           ###
#############################################

run = True
while run:

    # Prompt the user to input the quantity of items & state, if anything other than the valid states acceptable or a number less than 0, then perform error check.
    item_quantity = int(input('Enter the quantity of items purchased: '))

    # Loop error check, until acceptable input is inputted.
    while item_quantity <= 0:
        item_quantity = int(input('Invalid Input! Quantity must be greater than 0: '))

    valid_state = input('Enter a valid state (CA, NV, AZ): ').upper()

    while valid_state not in ('CA', 'NV', 'AZ'):
        valid_state = input('Invalid State! Enter a valid state (CA, NV, AZ): ').upper()

    state_tax = calculate_state_tax(valid_state)
    items_discount = calculate_discount(item_quantity)

    gross_cost = item_quantity * 1
    discount_amount = gross_cost * items_discount
    net_cost = gross_cost - discount_amount
    tax_amount = net_cost * state_tax
    after_tax = net_cost + tax_amount


    # Discount applied identifier

    if item_quantity > 9 and item_quantity < 20:
	    print('\n5% discount\n')
    elif item_quantity > 19:
	    print('\n10% discount\n')
    else:
         print('No Discount Applied')


    # Format & Print the calculations - This will format each output respective to their own value.
    print('{:<16s} {:>8.2f}'.format('Gross Cost:', gross_cost))
    print('{:<16s} {:>8.2f}'.format('Discount:', discount_amount))
    print('{:<16s} {:>8.2f}'.format('Net Cost:', net_cost))
    print('{:<16s} {:>8.2f}'.format('Tax:', tax_amount))
    print('{:<16s} {:>8.2f}'.format('After Tax:', after_tax))



    # End the main program loop 

    run = False

 
        



