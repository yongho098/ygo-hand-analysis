import os
from time import sleep
from parameters import set_parameter
from simulator import simulator
from deck_editor import deck_edit

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

list1 = {'pank': 1, 'fenrir': 2, 'gryphon': 1, 'aegerine': 3, 'bluetang': 3, 'pascalus': 2, 'springirl': 3, 'enchantress': 3, 'sea horse': 3,
         'mandarin': 2, 'dark ruler': 3, 'cradle': 2, 'dive': 2, 'rite': 1, 'talents': 3, 'econ': 3, 'fateful': 1, 'battle ocean': 1,
         'dracoback': 1, 'wave': 1}

# sample decklist
test = """Monster
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


main_menu_options = {1: 'Run simulation', 2: 'Edit Deck', 3: 'Set Parameters', 4: 'Exit'}

def print_menu():
    for key in main_menu_options.keys():
        print(key, '--', main_menu_options[key])

def main_menu():
    print_menu()
    try:
        option = int(input('Enter choice: '))
    except ValueError:
        print("invalid input")
        return True
    if option == 1:
        sleep(0.1)
        os.system('cls')
        simulator()
    elif option == 2:
        sleep(0.1)
        os.system('cls')
        deck_edit()
    elif option == 3:
        sleep(0.1)
        os.system('cls')
        set_parameter()
    elif option == 4:
        quit()
    else:
        print('invalid menu')

while(True):
    main_menu()