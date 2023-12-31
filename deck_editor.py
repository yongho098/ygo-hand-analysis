import os
from time import sleep
import pyperclip
import json
import pprint



# add an import from file option so user doesnt have to do manually every time
#run create card when booting for default?
# json for decklist, classifications? share same name so can identify

# have load function also load classification
# run load function at runtime-create separate funciton

deck_list = []
deck_list_clean = []
card_object_list = []
card_type = []
card_subtype = []
# main deck only
deck_dictionary_main = {}
deck_dictionary_whole = {}
output_path = ""

with open("decklists/example_decklist.json") as json_file:
        json_data = json.load(json_file)
output_path = 'example_decklist'


deck_edit_menu_options = {1: 'Select Deck', 2: 'Import Deck', 3: 'View Deck', 4: 'Return'}
def print_menu():
    for key in deck_edit_menu_options.keys():
        print(key, '--', deck_edit_menu_options[key])

def parser(decklist, mode):
    # might need 2 parser functions for whole and only main. or make a mode switch
    # add to local then overwrite real if valid
    # categorize on creation? should leave it to 
    global deck_dictionary_whole, deck_dictionary_main
    if mode == 'whole':
        local_dict_whole = {}
        for i in range(len(decklist)-1):
            if decklist[i][0].isnumeric():
                local_dict_whole[decklist[i][2:]] = int(decklist[i][0])
        # check if valid
        #print(local_dict_whole)
        if local_dict_whole != {}:
            deck_dictionary_whole.clear()
            deck_dictionary_whole = local_dict_whole.copy()
            return 1
        else:
            return 0
    elif mode == 'main':
        local_dict_main = {}
        for i in range(len(decklist)-1):
            if decklist[i] == 'Extra':
                # only add main deck
                break
            elif decklist[i][0].isnumeric():
                local_dict_main[decklist[i][2:]] = int(decklist[i][0])
        # return correct dictionary
        if local_dict_main != {}:
            deck_dictionary_main.clear()
            deck_dictionary_main  = local_dict_main.copy()
            return 1
        else:
            return 0
 
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
        # Starter, extender, defensive, offensive, garnet, consistency
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

def load_classification(card_obj_list, out_path):
    if os.path.exists(f"classification/{out_path}.json"):
        with open(f"classification/{out_path}.json") as json_file:
            classification_data = json.load(json_file)
        for card in card_obj_list:
            if card.name in classification_data:
                card.card_type = classification_data[card.name][1]
                card.subtype = classification_data[card.name][2]
        return card_obj_list
    return card_obj_list

def deck_selector():
    # toss loader in here too
    global deck_dictionary_main, card_object_list, output_path
    options = os.listdir('decklists')
    while(True):
        for i in range(len(options)):
            print(f"{i + 1} -- {options[i]}")
        try:
            selection = int(input('Select Decklist to Load: '))
        except ValueError:
            sleep(0.1)
            os.system('cls')
            print("Invalid Input")
        if selection > len(options):
            sleep(0.1)
            os.system('cls')
            print('Invalid Input')
            continue
        else:
            # load deck
            select_path = f"decklists/{options[selection - 1]}"
            output_path = options[selection - 1][:-5]
            input("Selected deck. press Enter to Continue.")
            with open(select_path) as json_file:
                json_data = json.load(json_file)
            deck_dictionary_main = json_data
            card_object_list.clear()
            create_card()
            deck_list_clean.clear()
            card_object_list = load_classification(card_object_list, output_path)
            for key in deck_dictionary_main:
                deck_list_clean.append(key)
            sleep(0.1)
            os.system('cls')
            return



def deck_importer():
    global card_object_list
    input('Copy Omega decklist into clipboard. Press Any Button to continue')
    input_decklist = pyperclip.paste()
    sleep(0.1)
    os.system('cls')
    deck_list = input_decklist.split("\r\n")
    parser(deck_list, 'whole')
    success = parser(deck_list, 'main')
    
    if success == 1:
        # valid decklist-create json
        for key in deck_dictionary_main:
            deck_list_clean.append(key)
        print(deck_dictionary_whole)
        card_object_list.clear()
        create_card()
        json_object = json.dumps(deck_dictionary_main, sort_keys=True, indent=4)
        # make global to access outside
        output_path = input("Input Decklist Name: ")
        with open(f"decklists/{output_path}.json", "w") as outfile:
            outfile.write(json_object)
        input('Imported Decklist to decklists Folder. Press Enter to continue')
        sleep(0.1)
        os.system('cls')
        return
    else:
        # tried to add invalid deck
        input("Invalid Deck Format. Press Enter to continue")
        sleep(0.1)
        os.system('cls')
        return

def viewer(deck_dict):
    pprint.pprint(deck_dict)
    input("Viewing Deck List. Press Enter to continue.")
 
# main function       
def deck_edit():
    while(True):
        print_menu()
        try:
            option = int(input('Enter Option: '))
        except ValueError:
            sleep(0.1)
            os.system('cls')
            print("Invalid Option")
            continue
        # Select deck from decklist folder-already imported.
        if option == 1:
            # select deck
            # change dictionary to it and create cards
            sleep(0.1)
            os.system('cls')
            deck_selector()

        # copies deck from clipboard, need to make sure only grabbing main deck
        # should implement decklist select to circumvent? -load jsons
        # if successful creation then write to a json
        # should get submenu option or default to given decklist-select deck in parameters?
        elif option == 2:
            # reformat into a function
            # add an export to json option
            sleep(0.1)
            os.system('cls')
            deck_importer()
            sleep(0.1)
            os.system('cls')

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
            return card_object_list, output_path
        # invalid option
        else:
            sleep(0.1)
            os.system('cls')
            print('Invalid Menu Option')
            continue

deck_dictionary_main = json_data
card_object_list.clear()
create_card()

deck_list_clean.clear()
for key in deck_dictionary_main:
    deck_list_clean.append(key)
card_object_list = load_classification(card_object_list, 'example_decklist')
