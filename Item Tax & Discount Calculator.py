# Project 1

# The Dollar Store: A store sells all items for $1. The store has the following rules

# Discount Rules:
# Customers buying 10 or more items receive a 5% discount
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

# CALCULATE STATE TAX
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

# CALCULATE DISCOUNT
# This will calculate the discount to be applied based on the quantity of items entered.
def calculate_discount(item_quantity):
    if item_quantity >= 20:
        return 0.10
    elif item_quantity >= 10:
        return 0.05
    else:
        return 0
    
# USER INPUT FOR ITEM QUANTITY
# This will prompt and get the quantity from the user and error check at the same time.
def fetch_item_quantity():
    item_quantity = int(input('\nEnter the quantity of items purchased: '))

    # Error check
    while item_quantity <=0:
        item_quantity = int(input('\nInvalid Input! Quantity must be greater than 0: '))
    return item_quantity

# USER INPUT FOR STATE
# This will prompt and get the applicable state of purchase from the user and error check if state is valid.
def fetch_valid_state():
    valid_state = input('Enter a valid state (CA, NV, AZ): ').upper()

    # Error check
    while valid_state not in ('CA', 'NV', 'AZ'):
        valid_state = input('\nInvalid State! Enter a valid state (CA, NV, AZ): ').upper()
    return valid_state

# CALCULATE TOTALS
# This will calculate all totals then return the values for later printing in another function.
def calculate_all_totals(item_quantity, valid_state):
    state_tax = calculate_state_tax(valid_state)
    items_discount = calculate_discount(item_quantity)
    gross_cost = item_quantity * 1
    discount_amount = gross_cost * items_discount
    net_cost = gross_cost - discount_amount
    tax_amount = net_cost * state_tax
    after_tax = net_cost + tax_amount
    return gross_cost, discount_amount, net_cost, tax_amount, after_tax

# PRINT REPORT
# This will be the print function, that prints all calculated totals from the 'calculate_all_totals' function and format it accordingly.
def print_totals(gross_cost, discount_amount, net_cost, tax_amount, after_tax, item_quantity):
    
    # Discount applied identifier
    discount_message = '\nNo Discount Applied.\n' if item_quantity < 10 else '\n5% Discount Applied.\n' if item_quantity < 20 else '\n10% Discount Applied.\n'

     # Format & Print the calculations
    print(discount_message)
    print(format(f'Gross Cost:', '18s'), format(gross_cost, '8.2f'))
    print(format(f'Discount:', '18s'), format(discount_amount, '8.2f'))
    print(format(f'Net Cost:', '18s'), format(net_cost, '8.2f'))
    print(format(f'Tax:', '18s'), format(tax_amount, '8.2f'))
    print(format(f'After tax:', '18s'), format(after_tax, '8.2f'))

# MAIN FUNCTION
# This will perform a main loop -- loops the code until user is finished.
def main_loop():
    while True:
        item_quantity = fetch_item_quantity()
        valid_state = fetch_valid_state()
        calculate_costs = calculate_all_totals(item_quantity, valid_state)
        print_totals(*calculate_costs, item_quantity)

        # Prompt the user to continue the loop by entering another calculation or exit the program.
        main_choice = input('\nWould you like to perform another calculation? (Y/N): ').upper()

        # Error check
        while main_choice not in ('Y', 'N'):
            main_choice = input('\nInvalid Input! Enter \'Y\' to continue or \'N\' to exit the program: ').upper()

        if main_choice =='N':
            exit()
        

########################################
###           MAIN PROGRAM           ###
########################################
            
main_loop()


