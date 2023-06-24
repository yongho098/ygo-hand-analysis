import os
from time import sleep
from deck_editor import deck_list_clean

#add choose deck option, based on decklist folder
parameter_menu_options = {1: 'Categorize', 2: 'Group', 3: 'Return'}
categorizer_menu_options = {1: 'Edit Card', 2: 'Return'}
grouper_menu_options = {}

def print_menu(dict):
    for key in dict.keys():
        print(key, '--', dict[key])

def categorizer(card_obj_list):
    sleep(0.1)
    os.system('cls')
    # just show list of cards and edit
    for i in range(len(deck_list_clean)):
        print(f"{i + 1}: {deck_list_clean[i]}")
    selection = int(input('Input Card to edit: ')) - 1
    # value error for returning
    # error check to make sure inside range
    sleep(0.1)
    os.system('cls')
    for card in card_obj_list:
        if card.name == deck_list_clean[selection]:
            card.card_type = 'Engine'
            card.subtype = 'Starter'
            #print(card.name)
    # show all vs just single copy?
    # showing all gives more full data
    for card2 in card_obj_list:
        print(f"{card2.name} -- {card2.card_type} -- {card2.subtype}")
    input("Press Enter to return")
    pass


# set list of objects as input
def set_parameter(card_obj_list):
    while(True):
        print_menu(parameter_menu_options)
        try:
            option = int(input('Enter choice: '))
        except ValueError:
            sleep(0.1)
            os.system('cls')
            print("invalid input")
            continue
        # categorize
        if option == 1:
            # needs sub menu
            categorizer(card_obj_list)
        # create groups
        elif option == 2:
            pass
        # return to main menu
        elif option == 3:
            sleep(0.1)
            os.system('cls')
            return
        else:
            sleep(0.1)
            os.system('cls')
            print('invalid menu option')