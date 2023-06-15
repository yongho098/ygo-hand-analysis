import os
from time import sleep
# runs the algorithm
# displays results

run_amount = 0
simulator_menu_options = {1: 'Run', 2: 'Number of runs'}
def print_menu():
    for key in simulator_menu_options():
        print(key, '--', simulator_menu_options[key])

def simulator():
    print('inside simulator')
    print_menu()