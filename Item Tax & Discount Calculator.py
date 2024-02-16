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
while True:

    # Prompt the user to input the quantity of items & state, if anything other than the valid states acceptable or a number less than 0, then perform error check.
    item_quantity = int(input('\nEnter the quantity of items purchased: '))

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

    if item_quantity >= 10 and item_quantity < 20:
        print('\n5% Discount Applied.\n')
    elif item_quantity >= 20:
        print('\n10% Discount Applied.\n')
    else:
        print('\nNo Discount Applied.\n')

    # Format & Print the calculations
    
    print(format(f'Gross Cost:', '18s'), format(gross_cost, '8.2f'))
    print(format(f'Discount:', '18s'), format(discount_amount, '8.2f'))
    print(format(f'Net Cost:', '18s'), format(net_cost, '8.2f'))
    print(format(f'Tax:', '18s'), format(tax_amount, '8.2f'))
    print(format(f'After tax:', '18s'), format(after_tax, '8.2f'))


    # Prompt the user if they'd like to make another calculation 

    main_choice = input('\nWould you like to perform another calculation? (Y/N): ').upper()
    while main_choice not in ('Y', 'N'):
        main_choice = input('Invalid Input! Enter \'Y\' to continue or \'N\' to exit the program: ').upper()

    if main_choice =='N':
        exit()

