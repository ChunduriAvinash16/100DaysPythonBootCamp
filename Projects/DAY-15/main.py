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
}

profit = 0


def print_resource():
    """
     To print the available resources
    :return:
    """
    print(f"Water:{resources['water']}ml")
    print(f"Milk:{resources['milk']}ml")
    print(f"Coffee:{resources['coffee']}mg")
    print(f"Money:{profit}$")


def process_coins():
    """
        Calculate the total amount given by
        customer
    :return: total amount
    """
    no_of_quarters = int(input("how many quarters?: "))  # 0.25
    no_of_dimes = int(input("how many dimes?: "))  # 0.10
    no_of_nickles = int(input("how many nickles?: "))  # 0.05
    no_of_pennies = int(input("how many pennies?: "))  # 0.01
    total_amount_given = no_of_quarters * 0.25 + no_of_dimes * 0.10 + no_of_nickles * 0.05 + no_of_pennies * 0.01
    return total_amount_given


def resource_check(flavor):
    """
        Check whether required ingredients are available or not
    :param flavor:
    :return:
    """
    ingredients = MENU[flavor]['ingredients']
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
        

def make_coffee(flavor):
    """
        reduce the resources based on the flavor selected
    :param flavor:
    :return:
    """
    ingredients = MENU[flavor]['ingredients']
    resources['water'] -= ingredients['water']
    resources['milk'] -= ingredients['milk']
    resources['coffee'] -= ingredients['coffee']


def transaction_successful(money_received,drink_cost):
    global profit
    """
        Returns true if payment is processed or else False.
    :param money_received:
    :param drink_cost:
    :return:
    """
    if money_received >= drink_cost:
        change = money_received - drink_cost
        print("Here is ${:.2f} in change.".format(change))
        profit += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money.Money refunded")


def coffee_vending(flavor):
    global profit
    if resource_check(flavor):
        total_amount_given = process_coins()
        total_cost = MENU[flavor]["cost"]
        if transaction_successful(total_amount_given,total_cost):
            make_coffee(flavor)


def coffee_machine():
    is_on = True
    while is_on:
        choice = input(" What would you like ?(espresso/latte/cappuccino)")
        if choice == "off":
            is_on = False
        elif choice == 'report':
            print_resource()
        else:
            coffee_vending(choice)

coffee_machine()
