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

profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def printReport():
    print(f"Water {resources['water']}")
    print(f"Milk {resources['milk']}")
    print(f"Coffee {resources['coffee']}")
    print(f"Total Amount {profit}")

def isResourceSufficient(orderIngredients):
    for i in orderIngredients:
        if orderIngredients[i]>=resources[i]:
            print(f"Sorry there is not enough {i}")
            return False
    return True

def processCoins():
    print("Enter coins.")
    total=int(input("quarters "))*0.25
    total+=int(input("dimes "))*0.1
    total+=int(input("nickles "))*0.05
    total+=int(input("pennies "))*0.01
    return total

def isTransactionSuccessful(recievedAmount, drinkCost):
    if recievedAmount<drinkCost:
        print("Insufficient Amount")
        return False
    else:
        change=round(recievedAmount-drinkCost,2)
        print(f"Refundable amount is {change}")
        global profit
        profit += drinkCost
        return True

def makeCoffee(drinkName, orderIngredients):
    for i in orderIngredients:
        resources[i] -= orderIngredients[i]
    print(f"Here is your {drinkName}")

isCoffee=True
while isCoffee:
    coffeeName=input("Enter coffee name ")
    if coffeeName=='off':
        isCoffee=False
    elif coffeeName=='report':
        printReport()
    else:
        drink=MENU[coffeeName]
        if isResourceSufficient(drink["ingredients"]):
            payment=processCoins()
            if isTransactionSuccessful(payment,drink["cost"]):
                makeCoffee(coffeeName, drink["ingredients"])


                
