# Lyric Love
# Apr. 26
# Final Project

# This program will serve as a contacts book/holder, it will allow the user to add, edit, and/or delete contacts to view at anytime.


contactsLists = [['Bob Wilson', '8856565', 'bob@aol.com'],
                 ['Mary Smith', '8858969', 'ms@aol.com'],
                 ['Joan Abby', '6568989', 'abby@gmail.com']]



# User Greeting

print('\nWelcome to your contacts program!')
print('This program will allows you to add, edit, or delete new/existing contacts whenever you please.\n')
print('Please type A to add a contact.')
print('Please type E to edit a contact.')
print('Please type D to delete a contact.')
print('Please type L to list all of your contacts.')
print('Please type H to get help.')
print('Please type X to exit the program.')

# Main Program Loop
run = True
while run == True:

    # Get the user input for what they want to do.
    mainChoice = input('\nPlease enter the action you would like to do: ').upper()

    while mainChoice not in ('A', 'E', 'D', 'L', 'H', 'X'):
        mainChoice = input('INPUT ERROR! Please only enter a valid character for an action: ').upper()

    if mainChoice == 'A':
        name = input('Please enter the name of the contact: ')
        phone = input('Please enter the phone number of the contact: ')
        eMail = input('Please enter the contacts email: ')

        contactsLists.append([name, phone, eMail])

        print(f'\n{name} has been successfully added to your contacts.')

    # Editing A Contact. . .

    elif mainChoice == 'E':
        errorCheckList = []

        # Get user input for the contact they'd like to edit.
        choice = input('\nWould you like to edit the contacts (N)ame, (P)hone Number, or (E)mail: ').lower()


        while choice not in ('n', 'p', 'e'):
            choice = input('\nINPUT ERROR! Please only enter one the options above (N|P|E): ').lower()

        # Editing a contact by name.

        if choice == 'n':

            for mainIndex in contactsLists:
                errorCheckList.append(mainIndex[0])

            name = input("Please enter the contacts name you'd like to edit: ")

            # Error Check user input
            while name not in errorCheckList:
                print('\nName not found! No action taken. \n')
                name = input("Please enter the contacts name you'd like to edit: ")


            for mainIndex in contactsLists:
                if name == mainIndex[0]:

                    # Get the new contact name from user input.
                    newName = input('Please enter a new name for this contact: ')
                    
                    # Override the old name with the new name.
                    mainIndex[0] = newName

                    print('\nContact updated.')

        # Editing a contacts phone number.

        elif choice == 'p':
            
            for mainIndex in contactsLists:
                errorCheckList.append(mainIndex[1])

            phone = input("Please enter the contacts phone number you'd like to edit: ")

            # Error Check user input
            while phone not in errorCheckList:
                print('\nPhone Number not found! No action taken. \n')
                phone = input("Please enter the contacts name you'd like to edit: ")


            for mainIndex in contactsLists:
                if phone == mainIndex[1]:

                    # Get the new contact phone number from user input.
                    newPhone = input('Please enter a new number for this contact: ')
                    
                    # Override the old phone number with the new phone number.
                    mainIndex[1] = newPhone

                    print('\nContact updated.')

        # Editing a contacts E-Mail.

        else:
            
            for mainIndex in contactsLists:
                errorCheckList.append(mainIndex[2])

            eMail = input("Please enter the contacts E-Mail you'd like to edit: ")

            # Error Check user input
            while eMail not in errorCheckList:
                print('\nE-Mail not found! No action taken. \n')
                eMail = input("Please enter the contacts E-Mail you'd like to edit: ")


            for mainIndex in contactsLists:
                if eMail == mainIndex[2]:

                    # Get the new contact phone number from user input.
                    newEmail = input('Please enter a new E-Mail for this contact: ')
                    
                    # Override the old phone number with the new phone number.
                    mainIndex[2] = newEmail

                    print('\nContact updated.')

    # Deleting a contact from the list.

    elif mainChoice == 'D':
        errorCheckList = []
        choice = input('\nWould you like to remove the person by (N)ame, (P)hone Number, or (E)mail: ').lower()

        # Error check user input.
        while choice not in ('n', 'p', 'e'):
            choice = input('\nINPUT ERROR! Please only enter one the options above (N|P|E): ').lower()

        # Deleting a contact by name.

        if choice == 'n':

            for mainIndex in contactsLists:
                errorCheckList.append(mainIndex[0])

            name = input('Please enter the contacts name: ')

            # Error check user input.
            while name not in errorCheckList:
                print('\nName not found. No action taken.\n')
                name = input('Please enter a valid name: ')

            for mainIndex in contactsLists:
                if name == mainIndex[0]:
                    del mainIndex[2]
                    del mainIndex [1]
                    del mainIndex[0]

                    contactsLists = list(filter(None, contactsLists))

                    print('\nContact removed.')

        # Deleting a contact by phone number.

        elif choice == 'p':

            for mainIndex in contactsLists:
                errorCheckList.append(mainIndex[1])

            phone = input('Please enter the contacts Phone Number: ')

            # Error check user input.
            while phone not in errorCheckList:
                print('\nPhone Number not found. No action taken.\n')
                phone = input('Please enter a valid Phone Number: ')

            for mainIndex in contactsLists:
                if phone == mainIndex[1]:
                    del mainIndex[2]
                    del mainIndex[1]
                    del mainIndex[0]


                    contactsLists = list(filter(None, contactsLists))

                    print('\nContact removed.')

        # Deleting contact by E-Mail.

        else:

            for mainIndex in contactsLists:
                errorCheckList.append(mainIndex[2])

            eMail = input('Please enter the contacts Email: ')

            # Error check user input.
            while eMail not in errorCheckList:
                print('\nE-Mail not found. No action taken.\n')
                eMail = input('Please enter a valid Email: ')

            for mainIndex in contactsLists:
                if eMail == mainIndex[2]:
                    del mainIndex[2]
                    del mainIndex[1]
                    del mainIndex[0]

                    contactsLists = list(filter(None, contactsLists))

                    print('\nContact removed.')

    # Listing all contacts saved.

    elif mainChoice == 'L':
        for mainIndex in contactsLists:
            name = mainIndex[0]
            phone = mainIndex[1]
            eMail = mainIndex[2]

            print('---------------------------------------------------------')
            print(f'Name:   {name}')
            print(f'Number: {phone}')
            print(f'E-Mail: {eMail}')
            print('---------------------------------------------------------')

    # User Help

    elif mainChoice == 'H':

        print('\nPlease type A to add a contact.')
        print('Please type E to edit a contact.')
        print('Please type D to delete a contact.')
        print('Please type L to list all of your contacts.')
        print('Please type H to get help.')
        print('Please type X to exit the program.\n')

    # Exiting Program/Closing main program loop and prompting a goodbye message.

    else:
        run = False
        print('\nHave a nice day!!!')  
