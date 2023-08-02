import os
from time import sleep
from deck_editor import deck_list_clean

#add choose deck option, based on decklist folder
# Starter, extender, defensive, offensive, garnet, consistency
parameter_menu_options = {1: 'Categorize', 2: 'Group', 3: 'Return'}
categorizer_menu_options = {1: 'Edit Card', 2: 'Return'}
categorizer_submenu_options = {1: 'Engine', 2: 'Non-Engine', 3: 'Starter', 4: 'Extender', 5: 'Defensive', 6: 'Offensive', 7: 'Garnet', 8: 'Consistency', 9: 'Return'}
grouper_menu_options = {}

def print_menu(dict):
    for key in dict.keys():
        print(key, '--', dict[key])

def sub_categorizer(card_obj_list):
    card_type = ''
    card_subtype = ''
    while(True):
            sleep(0.1)
            os.system('cls')
            print_menu(categorizer_submenu_options)
            try:
                sub_selection = int(input('Select Category: '))
            except ValueError:
                sleep(0.1)
                os.system('cls')
                print("Invalid Option")
                continue
            if sub_selection == 1 or sub_selection == 2:
                card_type = categorizer_submenu_options[sub_selection]
            elif sub_selection == 9:
                sleep(0.1)
                os.system('cls')
                break
            else:
                card_subtype = categorizer_submenu_options[sub_selection]
    return card_type, card_subtype

def categorizer(card_obj_list):
    while(True):
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
        
        result = sub_categorizer(card_obj_list)
        sleep(0.1)
        os.system('cls')
        
        categorize_amount = 0
        for card in card_obj_list:
            if card.name == deck_list_clean[selection]:
                card.card_type = result[0]
                card.subtype = result[1]
                categorize_amount+=1
                #print(card.name)
        # print(f'{deck_list_clean[selection]}: {categorize_amount}')

        for i in range(len(deck_list_clean)):
            for card3 in card_obj_list:
                if card3.name == deck_list_clean[i]:
                    print(f'{deck_list_clean[i]} -- Copies: {card3.amount} -- {card3.card_type} -- {card3.subtype}')
                    break
        input("Press Enter to return")
        # save to decklist? need a way to save. maybe make a separate json 'x-1, x-2'
        # have a reset option in there too
        pass


# set list of objects as input
def set_parameter(card_obj_list):
    while(True):
        print_menu(parameter_menu_options)
        try:
            option = int(input('Enter Option: '))
        except ValueError:
            sleep(0.1)
            os.system('cls')
            print("Invalid Option")
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
            print('Invalid Menu Option')