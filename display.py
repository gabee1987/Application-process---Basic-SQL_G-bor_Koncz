"""
    Basic SQL assaignment console display module.
    by Gabor Koncz
"""

from tabulate import tabulate


def print_table(table, headers):
    print(tabulate(table, headers, tablefmt="fancy_grid"))

HEADERS = {
            "Menu1": [
                    "Id",
                    "First name",
                    "Last name",
                    "Nickname",
                    "Phone number",
                    "Email",
                    "City",
                    "Favourite number"
                    ],
            "Menu2": [
                    "Id",
                    "First name",
                    "Last name",
                    "Phone number",
                    "Email",
                    "Application code"
                    ],
            "Menu3": [
                    "First name",
                    "Last name"
                    ],
            "Menu4": ["Nicknames"],
            "Menu5": [
                    "Full name",
                    "Phone number"
                    ],
            "Menu6": [
                    "Full name",
                    "Phone number"
                    ],
            "Menu7": [
                    "Id",
                    "First name",
                    "Last name",
                    "Phone number",
                    "Email",
                    "Application code"
                    ],
            "Menu8": [
                    "Full name",
                    "Phone number"
                    ]

            }