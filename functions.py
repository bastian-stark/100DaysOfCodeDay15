# Functions for main

import menu_data

def ask_choice():
    """Asks user for their order"""
    choice = input('What would you like? (Espresso/Latte/Cappuccino/Exit): ').lower()
    if choice == "espresso" or choice == "latte" or choice == "cappuccino" or choice == "report" or choice == "exit":
        return choice
    else:
        print('Invalid response, please try again. ')
        return ask_choice()

def ask_for_payment(cost):
    """Asks the user for payment, calculates if the payment amount is enough, and prints change amount"""
    print(f'Cost: ${cost}')
    print('Please insert coins. ')
    quarters = float(input('How many quarters?: '))
    dimes = float(input('How many dimes?: '))
    nickels = float(input('How many nickels?: '))
    pennies = float(input('How many pennies?: '))
    if ((quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)) < cost:
        print("Sorry, that's not enough money. ")
        return ask_for_payment(cost)
    elif (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01) > cost:
        change = ((quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)) - cost
        print(f'Here is ${round(change, 2)} in change.')
        return round(cost, 2)
    else:
        return round(cost, 2)