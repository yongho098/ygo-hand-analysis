import os
from time import sleep
import random
import csv
# get object list
# runs the algorithm
# displays results
# take categorizations as well in input
# import categorizations

results = []

run_amount = 5
hand_size = 5
# settings for categorizations?
simulator_menu_options = {1: 'Run', 2: 'Settings', 3: 'Return'}
# should have export options
results_menu_options = {1: 'Export to csv', 2: 'Export to txt file', 3: 'Return'}
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
    

def simulation(card_list, runs, hand_size):
    results = []
    for run in range(runs):
        local_result = []
        random.shuffle(card_list)
        # handsize
        for card in range(hand_size):
            local_result.append(card_list[card].name)
        print(local_result)
        results.append(local_result)
        # local results, add to global after printing
    print('\n')
    # export to csv
    # how to check if duplicate and whether to overwrite?
    # analysis here?
    if input("Press 1 to Export Results. ") == '1':
        export_name = input('Enter Export File Name: ')
        with open(f"results/{export_name}.csv", 'w') as file:
            for line in results:
                writer = csv.writer(file, lineterminator="\n")
                writer.writerow(sorted(line))
        input("Exported Results to results Folder. Press Enter to continue.")
        sleep(0.1)
        os.system('cls')
    else:
        sleep(0.1)
        os.system('cls')

def simulator(card_object_list):    
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
            simulation(card_object_list, run_amount, hand_size)
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
            