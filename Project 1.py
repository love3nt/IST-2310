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



# Creating a clear screen function using imported modules and defining the function.

def greeting_message(message, n):
    print(message)
    time.sleep(n)
    # Clearing the screen
    os.system('cls' if os.name == 'nt' else 'clear')

# This message will display for 5 seconds, clear screen, then proceed to main program loop
    
message = "\nWelcome!\n \nThis program calculates appropriate discount based on quantity purchased and corresponding sales tax based on state"
n = 5          
greeting_message(message,n)

# Begin Main Program Loop

run = True
while run == True:

    # Prompt the user to input the number of items purchased

    item_quanitity = int(input('Enter the quanity of items purchased: '))

    # Error check for quanity less then or equal to 0
    while item_quanitity <= 0:
        item_quanitity = int(input('Invalid Input! Quanity must be greater than 0: '))

     # Prompt the user to input a valid state (CA, AZ. NV)
        
    valid_state = str(input('Enter a valid state (CA, NV, AZ): ')).upper

    # Error check for a valid state 
    while valid_state not in (CA, NV, AZ):
        valid_state = str(input('Invalid State! Enter a valid state (CA, NV, AZ): '))

    if valid_state == CA:
        

    
        

