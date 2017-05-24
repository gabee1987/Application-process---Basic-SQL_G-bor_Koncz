"""
    Basic SQL assaignment menu handler module
    by Gabor Koncz
"""

import sys
import os
import time
from queries import *
from display import *

menu_actions = {}


def main_menu():
    """
        Displays the main menu,
        where the user can navigate with integer inputs.
    """
    os.system('clear')
    print("Welcome to Gabor Koncz's Application process - Basic SQL program\n")
    print("Please select an option\n")
    menu_options = [
                "Mentors Table",
                "Applicants Table",
                "Name of Mentors",
                "Nicknames of mentors working at Miskolc",
                "Carol\'s phone number who lost her hat",
                "The real owner of the hat",
                "New Applicant",
                "Jemima\'s new phone number",
                "Cancel application request"
                ]
    for index, option in enumerate(menu_options):
        print("({0}) {1}".format(index + 1, option))
    print("(0) {0}".format("Exit"))
    choice = input(" >>  ")
    execute_menu(choice)


def execute_menu(choice):
    """
        Handles the menu navigation,
        displays the appropiate menu.
    """
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions["main_menu"]
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            time.sleep(1)
            menu_actions['main_menu']
        except TypeError:
            print("Invalid selection, please try again.\n")
            time.sleep(1)
            menu_actions['main_menu']


# Menu options
def menu1():  # Shows all data from mentors table
    print("Mentors Table\n")
    print_table(mentors_all(), headers=HEADERS["Menu1"])
    print("To go back hit Enter without input")
    print("0. Quit")
    choice = input(" >>  ")
    execute_menu(choice)


def menu2():  # Shows all data from applicants table
    print("Applicants Table!\n")
    print_table(applicants_all(), headers=HEADERS["Menu2"])
    print("To go back hit Enter without input")
    print("0. Quit")
    choice = input(" >>  ")
    execute_menu(choice)


def menu3():  # Shows the first_name and last_name from mentors table
    print("Name of Mentors!\n")
    print_table(name_of_mentors(), headers=HEADERS["Menu3"])
    print("To go back hit Enter without input")
    print("0. Quit")
    choice = input(" >>  ")
    execute_menu(choice)


def menu4():  # Shows the nicknames of mentors from Miskolc
    print("Nicknames of mentors working at Miskolc!\n")
    print_table(nicknames_of_mentors(), headers=HEADERS["Menu4"])
    print("To go back hit Enter without input")
    print("0. Quit")
    choice = input(" >>  ")
    execute_menu(choice)


def menu5():  # Shows the full_name and phone_number of the girl who lost her hat
    print("Carol\'s phone number who lost her hat!\n")
    print_table(carols_phone_number(), headers=HEADERS["Menu5"])
    print("To go back hit Enter without input")
    print("0. Quit")
    choice = input(" >>  ")
    execute_menu(choice)


def menu6():  # Shows the full_name and phone_number of the real owner of the hat
    print("The real owner of the hat\n")
    print_table(real_owner_of_hat(), headers=HEADERS["Menu6"])
    print("To go back hit Enter without input")
    print("0. Quit")
    choice = input(" >>  ")
    execute_menu(choice)


def menu7():  # Creates and shows all the data of the new applicant
    print("New Applicant\n")
    new_applicant()
    print_table(new_applicant(), headers=HEADERS["Menu7"])
    print("To go back hit Enter without input")
    print("0. Quit")
    choice = input(" >>  ")
    execute_menu(choice)


def menu8():  # Updates and shows Jemima's new phone number
    print("Jemima\'s new phone number\n")
    jemimas_new_phone_number()
    print_table(jemimas_new_phone_number(), headers=HEADERS["Menu8"])
    print("To go back hit Enter without input")
    print("0. Quit")
    choice = input(" >>  ")
    execute_menu(choice)


def menu9():  # Deletes the datas with this email domain: @mauriseu.net
    print("Cancel application request\n")
    application_cancel()
    print("Data deleted!\n")
    print("To go back hit Enter without input")
    print("0. Quit")
    choice = input(" >>  ")
    execute_menu(choice)


def back():
    menu_actions["main_menu"]


def exit():
    sys.exit()


menu_actions = {
    "main_menu": main_menu,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    '4': menu4,
    '5': menu5,
    '6': menu6,
    '7': menu7,
    '8': menu8,
    '9': menu9,
    '0': exit,
    }
