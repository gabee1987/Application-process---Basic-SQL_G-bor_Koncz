import sys
import os
import psycopg2

menu_actions = {}


def main_menu():
    os.system('clear')
    print("Welcome to Gabor Koncz's Application process - Basic SQL program\n")
    print("Please select an option\n")
    menu_options = [
                'Mentors Table',
                'Applicants Table'
                'Name of Mentors',
                'Nicknames of mentors working at Miskolc',
                'Carol\'s phone number who lost her hat',
                'The real owner of the hat',
                'New Applicant',
                'Jemima\'s new phone number',
                'Cancel application request',
                ]
    for index, option in enumerate(menu_options):
        print("({0}) {1}".format(index + 1, option))
    print("(0) {0}".format('Exit'))
    choice = input(" >>  ")
    execute_menu(choice)


def execute_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main_menu']
        except TypeError:
            print("Invalid selection, please try again.\n")
            menu_actions['main_menu']



def menu1():
    print("Hello Menu 1 !\n")
    print("9. Back")
    print("0. Quit")
    choice = input(" >>  ")
    execute_menu(choice)



def menu2():
    print("Hello Menu 2 !\n")
    print("9. Back")
    print("0. Quit" )
    choice = input(" >>  ")
    execute_menu(choice)



def menu3():
    print("Hello Menu 2 !\n")
    print("9. Back")
    print("0. Quit" )
    choice = input(" >>  ")
    execute_menu(choice)



def menu4():
    print("Hello Menu 2 !\n")
    print("9. Back")
    print("0. Quit" )
    choice = input(" >>  ")
    execute_menu(choice)



def menu5():
    print("Hello Menu 2 !\n")
    print("9. Back")
    print("0. Quit" )
    choice = input(" >>  ")
    execute_menu(choice)



def menu6():
    print("Hello Menu 2 !\n")
    print("9. Back")
    print("0. Quit" )
    choice = input(" >>  ")
    execute_menu(choice)



def menu7():
    print("Hello Menu 2 !\n")
    print("9. Back")
    print("0. Quit" )
    choice = input(" >>  ")
    execute_menu(choice)



def back():
    menu_actions['main_menu']


def exit():
    sys.exit()




menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '9': back,
    '0': exit,
}


if __name__ == "__main__":
    main_menu()