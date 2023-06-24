import os
from time import sleep
import pyperclip
import json
import pprint

with open("decklists/example_decklist.json") as json_file:
        json_data = json.load(json_file)

# add an import from file option so user doesnt have to do manually every time
#run create card when booting for default?
# json for decklist, classifications? share same name so can identify

deck_list = []
deck_list_clean = []
card_object_list = []
card_type = []
card_subtype = []
# main deck only
deck_dictionary_main = {}
deck_dictionary_whole = {}

deck_edit_menu_options = {1: 'Select Deck', 2: 'Import Deck', 3: 'View Deck', 4: 'Return'}
def print_menu():
    for key in deck_edit_menu_options.keys():
        print(key, '--', deck_edit_menu_options[key])

def parser(decklist, mode):
    # might need 2 parser functions for whole and only main. or make a mode switch
    # categorize on creation? should leave it to user
    if mode == 'whole':
        for i in range(len(decklist)-1):
            if decklist[i][0].isnumeric():
                deck_dictionary_whole[decklist[i][2:]] = int(decklist[i][0])
    elif mode == 'main':
        for i in range(len(decklist)-1):
            # print(decklist[i])
            if decklist[i] == 'Extra':
                # only add main deck
                return
            elif decklist[i][0].isnumeric():
                deck_dictionary_main[decklist[i][2:]] = int(decklist[i][0])
 
# create objects for each card in main? allow user to assign/edit properties
# class card
# maybe add all attributes to future proof
class Card:
    # all card shared properties. currently none
    
    def __init__(self, name):
        # specific card
        self.name = name
        self.score = 1
        self.copy = 1
        # number in deck, default 1
        self.amount = 1
        # Either engine or non-engine since calcluating playability
        self.card_type = ''
        # applying Patrick Hoban's card type theory-turn into list since possible to have multiple
        # Starter, extender, defensive, garnet, consistency
        self.subtype = ''

# take dictionary and create objects out of it. add to list afterwards
# grab random 5 from list
def create_card():
    #for card_name, amount in test_dict.items():
    for card_name, amount in deck_dictionary_main.items():
        if amount == 1:
            new_card = Card(card_name)
            new_card.copy = 1
            new_card.amount = 1
            card_object_list.append(new_card)
        else:
            for i in range(amount):
                new_card = Card(card_name)
                new_card.copy = i+1
                new_card.amount = amount
                card_object_list.append(new_card)

def viewer(deck_dict):
    pprint.pprint(deck_dict)
    input("Viewing Deck List. Press Enter to continue.")
 
# main function       
def deck_edit():
    while(True):
        print_menu()
        try:
            option = int(input('Enter choice: '))
        except ValueError:
            sleep(0.1)
            os.system('cls')
            print("invalid input")
            continue
        # Select deck from decklist folder-already imported.
        if option == 1:
            sleep(0.1)
            os.system('cls')
            print(deck_dictionary_main)
            input('Viewing Main Deck. Press Enter to continue')
            sleep(0.1)
            os.system('cls')
        # copies deck from clipboard, need to make sure only grabbing main deck
        # assumes user isnt retarded and gives a proper format otherwise it wipes current decklist.
        # should implement decklist select to circumvent? -load jsons
        # if successful creation then write to a json
        # should get submenu option or default to given decklist-select deck in parameters?
        elif option == 2:
            sleep(0.1)
            os.system('cls')
            print('importing')
            input('Copy decklist into clipboard. Press Enter to continue')
            input_decklist = pyperclip.paste()
            sleep(0.1)
            os.system('cls')
            # this might cause an issue in formatting
            print('Importing Decklist')
            deck_dictionary_main.clear()
            card_object_list.clear()
            deck_list = input_decklist.split("\r\n")
            parser(deck_list, 'whole')
            parser(deck_list, 'main')
            
            for key in deck_dictionary_main:
                deck_list_clean.append(key)
            print(deck_dictionary_whole)
            create_card()
            input('Imported Decklist. Press Enter to continue')
            sleep(0.1)
            os.system('cls')
            # parse and convert
            continue
        # view deck
        elif option == 3:
            sleep(0.1)
            os.system('cls')
            viewer(deck_dictionary_main)
            sleep(0.1)
            os.system('cls')
        # return to main menu
        elif option == 4:
            sleep(0.1)
            os.system('cls')
            return
        # invalid option
        else:
            sleep(0.1)
            os.system('cls')
            print('invalid menu')
            continue

deck_dictionary_main = json_data
create_card()
