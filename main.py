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
}

money = 0

PENNIES = 0.01
NICKLE = 0.05
DIME = 0.1
QUARTER = 0.25


# generate a report of all the resources
#   loop through the resources dictionary and print the resource along with their quantity
def generate_report():
    print('--------------COFFE MACHINE RESOURCES--------------')
    for resource, quantity in resources.items():
        if resource == 'coffee':
            print(f'{resource}: {quantity}g')
        else:
            print(f'{resource}: {quantity}ml')
    print(f'Money: ${money}')


# check for sufficiency of resources to make a particular coffee
#  if the user decides to make a coffee, check the ingredients of the coffee chosen against the resources
#      and tell the user that they can either make coffee or can't based on the comparison
def check_sufficient_resources(drink):
    for item in drink['ingredients']:
        if drink['ingredients'][item] > resources[item]:
            print(f'There is not enough {item}')
            return False
    return True




# process the payment in coins
#  if the resources are efficient to make the chosen coffee, then ask the user to enter their money in coins
#     calculate the user's total payment made
def process_coins():
    while True:
        try:
            print('-------------------TIME TO PAY------------------')
            print('Please enter some coins.')
            total = int(input('How many quarters: ')) * QUARTER
            total += int(input('How many nickles: ')) * NICKLE
            total += int(input('How many pennies: ')) * PENNIES
            total += int(input('How many dimes: ')) * DIME
            return total
        except ValueError:
            print('That is not a number')



# ensure that the payment is successful and give the user change if they have entered more than enough for a coffee
#    make sure that the payment is enough to buy the chosen coffee and when they pay too much, return them their change
#    and when they don't have enough payment, then refund the user their money
def check_successful_transaction(money_paid, drink):
    if money_paid < drink['cost']:
        print('Sorry, that is not enough, Money refunded!')
        return False
    elif money_paid >= drink['cost']:
        change = money_paid - drink['cost']
        print(f'Here is ${round(change, 2)} in change')
        global money
        money += drink['cost']
        return True



# make the drink for the user
# once the payment is successful, then make the coffee for the user  and update the coffee resources
def make_coffee(drink, choice):
    for item in resources:
        if item in drink['ingredients']:
            resources[item] -= drink['ingredients'][item]
    print(f'Here is your {choice.title()} ☕, enjoy!')



# turn off the machine
#   when the user enters off the coffee machine turns off

machine_is_on = True
while machine_is_on:
    print('----------------Welcome to the coffee machine program------------------')
    action = input('What would you like to make (espresso/latte/cappuccino): ').lower().strip()
    if action == "off":
        machine_is_on = False
        print('Goodbye 🙂')
    elif action == 'report':
        generate_report()
    elif action in MENU:
        coffee = MENU[action]
        if check_sufficient_resources(coffee):
            payment = process_coins()
            if check_successful_transaction(payment, coffee):
                print('-----------Transaction successful-----------')
                make_coffee(coffee,action)
    else:
        print('\n' * 10)
        print('That is not in the Menu')


