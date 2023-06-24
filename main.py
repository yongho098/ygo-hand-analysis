import os
from time import sleep
from parameters import set_parameter
from simulator import simulator
from deck_editor import deck_edit, card_object_list

#force default decklist on boot?

# card pool-api
# deck creator-import option
# define deck
# define tester
# test
# results-show hands, show statistics

# start with cli menu

# pyqt-button, label, input box, combo box, radio
# layout managers
# menu options? deck edit, set paramteres, test

# categorization
# types: starter, bombs, defensive
# engine number

main_menu_options = {1: 'Run simulation', 2: 'Edit Deck', 3: 'Set Parameters', 4: 'Exit'}

def print_menu():
    for key in main_menu_options.keys():
        print(key, '--', main_menu_options[key])

def main_menu():
    print_menu()
    try:
        option = int(input('Enter choice: '))
    except ValueError:
        sleep(0.1)
        os.system('cls')
        print("invalid input")
        return True
    # simulation
    if option == 1:
        sleep(0.1)
        os.system('cls')
        print(len(card_object_list))
        simulator(card_object_list)
    elif option == 2:
        sleep(0.1)
        os.system('cls')
        deck_edit()
    elif option == 3:
        sleep(0.1)
        os.system('cls')
        set_parameter(card_object_list)
    elif option == 4:
        quit()
    else:
        sleep(0.1)
        os.system('cls')
        print('invalid menu')

while(True):
    main_menu()