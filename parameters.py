import os
from time import sleep

parameter_menu_options = {}
def print_menu():
    for key in parameter_menu_options.keys():
        print(key, '--', parameter_menu_options[key])

def set_parameter():
    print('inside parameters')
    print_menu()