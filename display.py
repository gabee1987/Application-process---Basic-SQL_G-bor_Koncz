from tabulate import tabulate


def print_table(table):
    print(tabulate(table, tablefmt="fancy_grid"))

