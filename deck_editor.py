import os
from time import sleep
import pyperclip

#sample dictionary
list1 = {'pank': 1, 'fenrir': 2, 'gryphon': 1, 'aegerine': 3, 'bluetang': 3, 'pascalus': 2, 'springirl': 3, 'enchantress': 3, 'sea horse': 3,
         'mandarin': 2, 'dark ruler': 3, 'cradle': 2, 'dive': 2, 'rite': 1, 'talents': 3, 'econ': 3, 'fateful': 1, 'battle ocean': 1,
         'dracoback': 1, 'wave': 1}

deck_list = []
deck_dictionary = {}

# sample decklist
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

deck_edit_menu_options = {1: 'Edit *Not Implemented*', 2: 'Import', 3: 'Return'}
def print_menu():
    for key in deck_edit_menu_options.keys():
        print(key, '--', deck_edit_menu_options[key])

def parser(decklist):
    for i in range(len(decklist)-1):
        if decklist[i][0].isnumeric():
            deck_dictionary[decklist[i][2:]] = int(decklist[i][0])

def deck_edit():
    while(True):
        print_menu()
        try:
            option = int(input('Enter choice: '))
        except ValueError:
            print("invalid input")
            continue
        if option == 1:
            sleep(0.1)
            os.system('cls')
            print('editing')
            continue
        elif option == 2:
            # copies deck from clipboard, need to make sure only grabbing main deck
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
            parser(deck_list)
            print(deck_dictionary)
            input('Imported Decklist. Press Enter to continue')
            # parse and convert
            continue
        elif option == 3:
            sleep(0.1)
            os.system('cls')
            return
        else:
            print('invalid menu')
            continue
