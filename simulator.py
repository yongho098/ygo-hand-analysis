import os
from time import sleep
# runs the algorithm
# displays results

run_amount = 0
simulator_menu_options = {1: 'Run', 2: 'Number of runs', 3: 'Return'}

def print_menu():
    for key in simulator_menu_options.keys():
        print(key, '--', simulator_menu_options[key])

def simulator():    
    while(True):
        print_menu()
        try:
            option = int(input('Enter choice: '))
        except ValueError:
            print("invalid input")
            continue
        if option == 1:
            pass
        elif option == 2:
            pass
        # return to main menu
        elif option == 3:
            sleep(0.1)
            os.system('cls')
            return
        else:
            print('invalid menu option')
            