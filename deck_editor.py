import os
from time import sleep
import pyperclip

#sample dictionary
test_dict = {'Kashtira Ogre': 1, 'Kashtira Unicorn': 2, 'Kashtira Fenrir': 3, 'Scareclaw Kashtira': 1, 
         'Dimension Shifter': 3, 'Raidraptor - Tribute Lanius': 1, 'Kashtira Riseheart': 2, 
         "Raider's Wing": 1, 'Ash Blossom & Joyous Spring': 2, 'Kashtiratheosis': 3, 'Pot of Prosperity': 3, 
         'Terraforming': 1, 'Triple Tactics Talent': 3, 'Enemy Controller': 3, 'Kashtira Birth': 3, 
         'Pressured Planet Wraitsoth': 3, 'Infinite Impermanence': 3, 
         'Kashtira Big Bang': 1, 'Kashtira Preparations': 1}

# add an import from file option so user doesnt have to do manually every time

deck_list = []
deck_list_clean = []
card_object_list = []
card_type = []
card_subtype = []
# main deck only
deck_dictionary_main = {}
deck_dictionary_whole = {}

# sample decklist-doesnt have any ed or side deck
oldtest = """Monster
1 Dinowrestler Pankratops
2 Kashtira Fenrir
1 Wandering Gryphon Rider
3 Icejade Ran Aegirine
3 Marincess Blue Tang
2 Marincess Pascalus
3 Marincess Springirl
3 Water Enchantress of the Temple
3 Marincess Sea Horse
2 Marincess Mandarin
Spell
3 Dark Ruler No More
2 Icejade Cradle
2 Marincess Dive
1 Rite of Aramesir
3 Triple Tactics Talent
3 Enemy Controller
1 Fateful Adventure
1 Marincess Battle Ocean
1 Dracoback, the Rideable Dragon
Trap
1 Marincess Wave"""

deck_edit_menu_options = {1: 'Edit/View Main Deck *Edit Not Implemented*', 2: 'Import Deck', 3: 'Return'}
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
 
# main function       
def deck_edit():
    while(True):
        print_menu()
        try:
            option = int(input('Enter choice: '))
        except ValueError:
            print("invalid input")
            continue
        # View Deck
        if option == 1:
            sleep(0.1)
            os.system('cls')
            print(deck_dictionary_main)
            input('Viewing Main Deck. Press Enter to continue')
            sleep(0.1)
            os.system('cls')
        # copies deck from clipboard, need to make sure only grabbing main deck
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
            deck_list = input_decklist.split("\r\n")
            parser(deck_list, 'whole')
            parser(deck_list, 'main')
            for key in deck_dictionary_main:
                deck_list_clean.append(key)
            print(deck_dictionary_whole)
            input('Imported Decklist. Press Enter to continue')
            sleep(0.1)
            os.system('cls')
            # parse and convert
            continue
        # return to main menu
        elif option == 3:
            sleep(0.1)
            os.system('cls')
            create_card()
            # for obj in card_object_list:
            #     if obj.name == 'Kashtira Unicorn' or obj.name == 'Pressured Planet Wraitsoth' or obj.name == 'Terraforming':
            #         obj.card_type = 'Starter'
            #     print(f"{obj.name} -- {obj.card_type}")
            # input('Press Enter to return')
            return
        # invalid option
        else:
            print('invalid menu')
            continue
