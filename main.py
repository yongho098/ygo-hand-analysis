import os
from time import sleep
from parameters import set_parameter
from simulator import simulator
from deck_editor import deck_edit, card_object_list, output_path

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
    global card_object_list, output_path
    # return objects
    print_menu()
    try:
        option = int(input('Enter Option: '))
    except ValueError:
        sleep(0.1)
        os.system('cls')
        print("Invalid Option")
        return True
    # simulation
    if option == 1:
        sleep(0.1)
        os.system('cls')
        simulator(card_object_list)
    # deck menu
    elif option == 2:
        sleep(0.1)
        os.system('cls')
        # deck_edit()
        card_object_list, output_path = deck_edit()
    # parameters -later
    elif option == 3:
        sleep(0.1)
        os.system('cls')
        set_parameter(card_object_list, output_path)
    # quit
    elif option == 4:
        quit()
    else:
        sleep(0.1)
        os.system('cls')
        print('Invalid Menu Option')

while(True):
    sleep(0.1)
    os.system('cls')
    main_menu()    