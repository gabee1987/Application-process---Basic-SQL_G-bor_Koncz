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
                    ]
            }