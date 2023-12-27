# Coffee Machine Project

import functions
import menu_data

machineState = True
money = 0
while machineState == True:
    choice = functions.ask_choice()
    if choice == "exit":
        print("Exiting...")
        machineState = False
    elif choice == "report":
        for key in menu_data.resources:
            print(f'{key}: {menu_data.resources[key]}ml')
        print(f'Money: ${money}')
    else:
        count = 0
        for key in menu_data.resources:
            if menu_data.resources[key] - menu_data.MENU[choice]["ingredients"][key] < 0:
                print(f"Not enough {key}. ")
                count += 1
            else:
                menu_data.resources[key] -= menu_data.MENU[choice]["ingredients"][key]
        if count == 0:
            money += functions.ask_for_payment(menu_data.MENU[choice]["cost"])
            print(f"Here is your {choice}! Enjoy! ")