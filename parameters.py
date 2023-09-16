import os, json
from time import sleep
from deck_editor import deck_list_clean

#add choose deck option, based on decklist folder
# Starter, extender, defensive, offensive, garnet, consistency

parameter_menu_options = {1: 'Categorize', 2: 'Group', 3: 'Return'}
categorizer_menu_options = {1: 'Edit Card', 2: 'Return'}
categorizer_submenu_options = {1: 'Engine', 2: 'Non-Engine', 3: 'Starter', 4: 'Extender', 5: 'Defensive', 6: 'Offensive', 7: 'Garnet', 8: 'Consistency', 9: 'Return'}
grouper_menu_options = {1: 'Create Combo', 2: 'View Combo', 3: 'Delete Combo', 4: 'Return'}
final_output = [{}, []]

def print_menu(dict):
    for key in dict.keys():
        print(key, '--', dict[key])
        
def read_parameter(card_list, out_path):
    # meant for runtime
    # read json and recreate card items, force when loading new decklist?
    # maybe just toss in global
    if os.path.exists(f"classification/{out_path}.json"):
        with open(f"classification/{out_path}.json") as json_file:
            classification_data = json.load(json_file)
        for card in card_list:
            if card.name in classification_data[0]:
                card.card_type = classification_data[0][card.name][1]
                card.subtype = classification_data[0][card.name][2]
        final_output[0] =  classification_data[0]
        final_output[1] = classification_data[1]
        return card_list
    else:
        return card_list

def sub_categorizer(card_obj_list):
    # secondary menu for categorizing
    # have visiual indicators of what youre categorizing
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

def categorizer(card_obj_list, output_path):
    # create categorization, save categorizations. - read in simulator? save locally? ( what if they change decks. reading at runtime makes more consistent.)
    # overwrite, use current deckname/deck
    # need read option for runtime.
    while(True):
        sleep(0.1)
        os.system('cls')
        # just show list of cards and edit
        
        for i in range(len(deck_list_clean)):
            for card3 in card_obj_list:
                if card3.name == deck_list_clean[i]:
                    print(f'{i+1}: {deck_list_clean[i]} -- Copies: {card3.amount} -- {card3.card_type} -- {card3.subtype}')
                    break
        print('\n')
        selection = int(input('Input Card to edit, Input 0 to return: ')) - 1
        # value error for returning
        # error check to make sure inside range
        sleep(0.1)
        os.system('cls')
        
        # return option-save as well? save as json
        if selection == -1:
            # create output json object-maybe make function
            json_out = {}
            for j in range(len(deck_list_clean)):
                for card4 in card_obj_list:
                    if card4.name == deck_list_clean[j]:
                        json_out[card4.name] = [card4.amount, card4.card_type, card4.subtype]
                        break
            final_output[0] = json_out
            # output formatting?
            
            json_object = json.dumps(final_output, indent=2)
            with open(f"classification/{output_path}.json", "w") as outfile:
                outfile.write(json_object)
            input('Saved Configurations')
            sleep(0.1)
            os.system('cls')
            return

        result = sub_categorizer(card_obj_list)
        sleep(0.1)
        os.system('cls')
        
        categorize_amount = 0
        for card in card_obj_list:
            if card.name == deck_list_clean[selection]:
                card.card_type = result[0]
                card.subtype = result[1]
                categorize_amount+=1
        pass

def combo_delete(current):
     sleep(0.1)
     os.system('cls')
     while(True):
         # input cleaning
        
        for i in range(len(current)):
            print(f'{i+1}: {current[i]}')
        print('\n')
        try:
            selection = int(input('Input Combo to delete, Input 0 to return: ')) - 1
        except ValueError:
            sleep(0.1)
            os.system('cls')
            print("Invalid Option")
            continue
        if selection == -1:
            return current
        elif selection >= len(current):
            sleep(0.1)
            os.system('cls')
            print("Invalid Option")
            continue
        del current[selection]

def create_combo(card_obj_list):
    # deal with adding same combo
    output = []
    sleep(0.1)
    os.system('cls')
    while(True):        
        for i in range(len(deck_list_clean)):
                for card3 in card_obj_list:
                    if card3.name == deck_list_clean[i]:
                        print(f'{i+1}: {deck_list_clean[i]}')
                        break
        print('\n')
        try:
            # input cleaning
            selection = int(input('Input Card to add to combo, Input 0 to return: ')) - 1
            if selection == -1:
                return output
            output.append(deck_list_clean[selection])
            sleep(0.1)
            os.system('cls')
            print(f'Added: {deck_list_clean[selection]} -- {output}')
            print('\n')
        except IndexError:
            sleep(0.1)
            os.system('cls')
            print('Invalid Input')
        except ValueError:
            sleep(0.1)
            os.system('cls')
            print('Invalid Input')
        
        

def combo(card_obj_list, output_path):
    # show list, create lists of combos
    # currently just fenrir/rise + spell
    add = []
    output = final_output[1]
    # sub menu-view, create, return
    while(True):
        sleep(0.1)
        os.system('cls')
        print_menu(grouper_menu_options)
        try:
            option = int(input('Enter Option: '))
        except ValueError:
            sleep(0.1)
            os.system('cls')
            print("Invalid Option")
            continue
        if option == 1:
            # create combo
            sleep(0.1)
            os.system('cls')
            add = create_combo(card_obj_list)
            if len(add) > 1:
                output.append(add)
        elif option == 2:
            # view combos
            sleep(0.1)
            os.system('cls')
            for i in range(len(output)):
                print(output[i])
            input("Viewing Combos. Press Enter to continue.")
        # delete
        elif option == 3:
            sleep(0.1)
            os.system('cls')
            output = combo_delete(output)
        elif option == 4:
            # return-output, save
            # save-refactor into json
            final_output[1] = output
            sleep(0.1)
            os.system('cls')
            json_object = json.dumps(final_output, indent=2)
            with open(f"classification/{output_path}.json", "w") as outfile:
                outfile.write(json_object)
            input('Saved Configurations')
            sleep(0.1)
            os.system('cls')
            return

# set list of objects as input
def set_parameter(card_obj_list, output_path):
    card_obj_list = read_parameter(card_obj_list, output_path)
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
            categorizer(card_obj_list, output_path)
        # create groups
        elif option == 2:
            combo(card_obj_list, output_path)
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