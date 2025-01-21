MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "money": 0.0
}

# TODO 1 Prompt user by asking “ What would you like? (espresso/latte/cappuccino):
# TODO 2 Turn OFF the Coffee Machine by off Prompt

def make_coffee():
    global choice
    choice= input("What would you like? (espresso/latte/cappuccino): ")
    if choice in MENU:
        if check_resources_sufficient():
            if process_coins():
                print(f"Making your {choice}")
                deducting_resources()
                report()
                print(f"Here is your {choice}. Enjoy!")

            else:
                return make_coffee()
    elif choice== "OFF":
        print("Turning off the Coffee Machine")
        return False

    elif choice=="report":
        report()
    else:
        print("Enter a Valid Input: ")
    make_coffee()
#TODO 3 Print The current resources

def report():
    print(f"Water available: {resources["water"]} ml")
    print(f"Milk available: {resources["milk"]} ml")
    print(f"Coffee available: {resources["coffee"]} g")
    print(f"Money available: ${resources["money"]} ")

# TODO 4 Checking for available resources for the chosen drink
def check_resources_sufficient():
    is_available= True
    for key,value in MENU[choice]["ingredients"].items():
        if resources[key]<value:
            is_available = False
            print(f"Sorry, There is not enough {key} ")
    return is_available

# TODO 5 Proceesing Coins
def process_coins():
    print("Please insert coins.")
    # Prompt the user to enter the number of each type of coin
    quarters = int(input("How many quarters? ($0.25 each): "))
    dimes = int(input("How many dimes? ($0.10 each): "))
    nickels = int(input("How many nickels? ($0.05 each): "))
    pennies = int(input("How many pennies? ($0.01 each): "))
    # Calculate the total monetary value of the coins
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    # Display the total amount inserted
    print(f"Total inserted: ${total:.2f}")
    # TODO 6 Check transaction successful
    if MENU[choice]["cost"]>total:
        print(f"{choice} costs {MENU[choice]["cost"]} but inserted only ${total}")
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif MENU[choice]["cost"]<total:
        change= round(total-MENU[choice]["cost"],2)
        resources["money"]+=MENU[choice]["cost"]
        print(f"Here is $ {change} dollars in change.")
        return True
    else:
        resources["money"] += MENU[choice]["cost"]
        return True

# TODO 7 Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”
def deducting_resources():
    for key,value in resources.items():
        if key in MENU[choice]["ingredients"]:
            resources[key]= resources[key]-MENU[choice]["ingredients"][key]
    print(resources)


# make_coffee()
make_coffee()
