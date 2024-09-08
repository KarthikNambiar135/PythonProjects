logo = """


 ██████╗ ██████╗ ███████╗███████╗███████╗███████╗    ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
██╔════╝██╔═══██╗██╔════╝██╔════╝██╔════╝██╔════╝    ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
██║     ██║   ██║█████╗  █████╗  █████╗  █████╗      ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
██║     ██║   ██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══╝      ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
╚██████╗╚██████╔╝██║     ██║     ███████╗███████╗    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝     ╚══════╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝
                                                                                                             


"""
print(logo)
#menu and resources dictionaries
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0
}
#function to refill resources
def refill():
    refill_resource = input("What do you want to refill?(water/milk/coffee): ").lower()
    amount = int(input("Please enter Quantity in mL: "))
    if refill_resource == 'water':
        resources['water'] += amount
    elif refill_resource == 'milk':
        resources['milk'] += amount
    elif refill_resource == 'coffee':
        resources['coffee'] += amount
    else:
        print("Invalid input, Restarting machine...")
        print("Restarted.")
#function to manage coins
def coins(ch):
    print(f"Cost: {MENU[ch]['cost']}")
    print("Please insert coins:")
    quarter = float(input("Quarters: "))
    dimes = float(input("Dimes: "))
    nickles = float(input("Nickles: "))
    pennies = float(input("Pennies: "))
    total = float((quarter*0.25)+(dimes*0.1)+(nickles*0.05)+(pennies*0.01))
    if total < MENU[ch]['cost']:
        no_money = True
        return no_money
    else:
        change = total - MENU[ch]['cost']
        print(f"Here is ${change} dollars in change.")
        no_money = False
        return no_money
#function to handle drink making
def make(ch):
    if resources['water'] < MENU[ch]['ingredients']['water']:
        print("Sorry, there is not enough Water.")
    elif resources['milk'] < MENU[ch]['ingredients']['milk']:
        print("Sorry, there is not enough Milk.")
    elif resources['water'] < MENU[ch]['ingredients']['water']:
        print("Sorry, there is not enough Coffee.")
    else:
        output = coins(ch)
        if output:
            print("Sorry, that's not enough money. Money Refunded Successfully.")
        else:
            resources['water'] = resources['water'] - MENU[ch]['ingredients']['water']
            resources['milk'] = resources['milk'] - MENU[ch]['ingredients']['milk']
            resources['coffee'] = resources['coffee'] - MENU[ch]['ingredients']['coffee']
            resources['profit'] += MENU[ch]['cost']
            print(f"Here's your {ch}. Enjoy!")
#on variable to indicate if the machine is on
on = True
#looping until the machine is on
while on:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee == 'off':
        print("Shutting Down...")
        on = False
    elif coffee == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Profit: {resources['profit']}")
    elif coffee == 'refill':
        refill()
    elif coffee == 'espresso' or coffee == 'latte' or coffee == 'cappuccino':
        make(coffee)
    else:
        print("Sorry, The specified item is not in our menu.")
