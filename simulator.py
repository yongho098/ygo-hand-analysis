import os
from time import sleep
import random
import csv
import json
# get object list
# runs the algorithm
# displays results
# take categorizations as well in input
# import categorizations

combo_data = []

results = []

run_amount = 5
hand_size = 5
# settings for categorizations?-performed in deck editor
simulator_menu_options = {1: 'Run', 2: 'Settings', 3: 'Return'}
# should have export options
results_menu_options = {1: 'Export Data', 2: 'Export Analysis', 3: 'Export Both', 4: 'Return'}
settings_menu_options = {1: 'Number of Runs', 2: 'Hand Size', 3: 'Return'}

def print_menu(menu_dict):
    for key in menu_dict.keys():
        print(key, '--', menu_dict[key])

def settings_menu():
    global run_amount, hand_size
    while(True):
        print_menu(settings_menu_options)
        print(f'Number of Runs: {run_amount}, Hand Size: {hand_size}')
        try:
            option = int(input('Enter Option: '))
        except ValueError:
            sleep(0.1)
            os.system('cls')
            print("Invalid Option")
            return
        if option == 1:
            # number of runs
            sleep(0.1)
            os.system('cls')
            run_amount = int(input('Enter number of runs: '))
            sleep(0.1)
            os.system('cls')
        elif option == 2:
            # hand size
            sleep(0.1)
            os.system('cls')
            hand_size = int(input('Enter Hand Size: '))
            sleep(0.1)
            os.system('cls')
        elif option == 3:
            sleep(0.1)
            os.system('cls')
            return
        else:
            sleep(0.1)
            os.system('cls')
            print('Invalid menu option')
            continue
    
def analysis_func(local_list, combo):
    # make copy of list and edit to check
    
    # [1 starter, total starter, garnets, playable]
    output = [0, 0, 0, 0, 0]
    for card in local_list:
        if card.subtype == 'Starter':
            # becomes playable
            output[0] = 1
            output[1] += 1
        if card.subtype == 'Garnet':
            output[2] += 1
        # add combo for playable later
        for subcombo in combo:
            if card.name in subcombo:
                # loop through rest?
                local_copy = subcombo
                local_copy.remove(card.name)
                if local_copy[0] in local_list:
                    # counts as 2 card combo
                    # count 2 hand combo once only?
                    pass
                pass
    if output[0] != 0:
        # playable
        output[3] = 1
    return output

def simulation(card_list, runs, hand_size, combo):
    # list of list?
    total_starter = 0
    analysis_dict = {'Hands with at least 1 Starter': 0, 
                'Hands with no Starters': 0,
                'Hands with Garnets': 0,
                'Average Starters in Hand': 0,
                '"Playable Hands"': 0,
                '"Unplayable Hands': 0,
                'Average Hand Playability': '0%'}
    results = []
    
    for run in range(runs):
        analysis_results = []
        local_result = []
        local_card = []
        random.shuffle(card_list)
        # handsize
        for card in range(hand_size):
            local_result.append(card_list[card].name)
            local_card.append(card_list[card])
        analysis_results = analysis_func(local_card, combo)
        analysis_dict['Hands with at least 1 Starter'] += analysis_results[0]
        total_starter += analysis_results[1]
        if analysis_results[1] == 0:
            analysis_dict['Hands with no Starters'] += 1
        analysis_dict['Hands with Garnets'] += analysis_results[2]
        analysis_dict['"Playable Hands"'] += analysis_results[3]
        playable_percent = analysis_dict['"Playable Hands"']/runs
        analysis_dict['Average Hand Playability'] = f'{playable_percent * 100}%'
        print(local_result)
        results.append(local_result)
        # local results, add to global after printing
    
    print('\n')
    print(f'Runs: {runs}')
    analysis_dict['Average Starters in Hand'] = total_starter/runs
    print(analysis_dict)
    print('\n')
    # have analysis in here
    # what to evaluate

    # analysis here?
    print_menu(results_menu_options)
    export_option = input("Enter Option: ")
    if export_option == '1':
        # Just data
        export_name = input('Enter Export File Name: ')
        with open(f"results/{export_name}.csv", 'w') as file:
            for line in results:
                writer = csv.writer(file, lineterminator="\n")
                writer.writerow(sorted(line))
            writer.writerow(['Total Runs', runs])
        input("Exported Results to results Folder. Press Enter to continue.")
        sleep(0.1)
        os.system('cls')
    elif export_option == '2':
        # Just analysis
        export_name = input('Enter Export File Name: ')
        with open(f"results/{export_name}.csv", 'w') as file:
            for key, value in analysis_dict.items():
                out = [key, value]
                writer = csv.writer(file, lineterminator="\n")
                writer.writerow(out)
            writer.writerow(['Total Runs', runs])
        input("Exported Results to results Folder. Press Enter to continue.")
        sleep(0.1)
        os.system('cls')
    elif export_option == '3':
        # Both-most common
        export_name = input('Enter Export File Name: ')
        with open(f"results/{export_name}.csv", 'w') as file:
            for line in results:
                writer = csv.writer(file, lineterminator="\n")
                writer.writerow(sorted(line))
            writer.writerow('\n')
            for key, value in analysis_dict.items():
                out = [key, value]
                writer.writerow(out)
            writer.writerow(['Total Runs', runs])
        input("Exported Results to results Folder. Press Enter to continue.")
        sleep(0.1)
        os.system('cls')

    else:
        sleep(0.1)
        os.system('cls')
        
        
def read_parameter(out_path):
    # loading combo data
    if os.path.exists(f"classification/{out_path}.json"):
        with open(f"classification/{out_path}.json") as json_file:
            classification_data = json.load(json_file)
        return classification_data[1]
        


def simulator(card_object_list, output_path):
    combo_data = read_parameter(output_path)    
    while(True):
        print_menu(simulator_menu_options)
        try:
            option = int(input('Enter Option: '))
        except ValueError:
            sleep(0.1)
            os.system('cls')
            print("Invalid Option")
            continue
        # run simulation
        if option == 1:
            sleep(0.1)
            os.system('cls')
            simulation(card_object_list, run_amount, hand_size, combo_data)
        # apply settings
        elif option == 2:
            try:
                sleep(0.1)
                os.system('cls')
                settings_menu()
                sleep(0.1)
                os.system('cls')
            except ValueError:
                print("Input a number")
                continue
        # return to main menu
        elif option == 3:
            sleep(0.1)
            os.system('cls')
            return
        # Invalid Menu option
        else:
            sleep(0.1)
            os.system('cls')
            print('Invalid Menu Option')
            continue
            