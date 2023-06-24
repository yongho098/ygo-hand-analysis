import os
from time import sleep
import random
# get object list
# runs the algorithm
# displays results

results = []

run_amount = 0
simulator_menu_options = {1: 'Run', 2: 'Number of runs', 3: 'Return'}
# should have export options
results_menu_options = {1: 'Export to csv', 2: 'Export to txt file', 3: 'Return'}

def print_menu():
    for key in simulator_menu_options.keys():
        print(key, '--', simulator_menu_options[key])

def simulation(card_list, runs):
    # create list?
    # reset results
    results = []
    for run in range(runs):
        local_result = []
        random.shuffle(card_list)
        # handsize
        for card in range(5):
            local_result.append(card_list[card].name)
        print(local_result)
        results.append(local_result)
        # local results, add to global after printing
    print('\n')
    # print(results)
    input('Press Enter to continue.')
    sleep(0.1)
    os.system('cls')

def simulator(card_object_list):    
    while(True):
        print_menu()
        try:
            option = int(input('Enter choice: '))
        except ValueError:
            sleep(0.1)
            os.system('cls')
            print("invalid input")
            continue
        if option == 1:
            sleep(0.1)
            os.system('cls')
            simulation(card_object_list, run_amount)
        # run amounts
        elif option == 2:
            try:
                sleep(0.1)
                os.system('cls')
                run_amount = int(input('Enter number of runs: '))
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
        else:
            sleep(0.1)
            os.system('cls')
            print('invalid menu option')
            