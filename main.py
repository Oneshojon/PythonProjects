MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "money": 0,
}

def refill():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    print("Resources refill done!!")

def process_coin():
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    print("Please insert coins.")
    try:
        q_c = int(input("how many quarters?: "))
        d_c = int(input("how many dimes?: "))
        n_c = int(input("how many nickles?: "))
        p_c = int(input("how many pennies?: "))
        total_amount = quarters * q_c + dimes * d_c + nickles * n_c + pennies * p_c
        return round(total_amount, 2)
    except ValueError:
        print("Invalid input! Please enter numbers only. No money processed.")
        return 0


# TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
while True:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if prompt == "off":
        break
    # TODO: 7. Refill resource
    elif prompt == 'refill':
        refill()
    # TODO: 3. Print report.
    elif prompt == "report":
        for i in resources:
            print(f"{i}: {resources[i]}")
    # TODO: 4. Check resources sufficient?
    elif prompt in ["espresso","latte", "cappuccino"]:
        for item in ['milk', 'water', 'coffee']:
            if resources[item] < MENU[prompt]["ingredients"][item]:
                print(f"Sorry there is not enough {item}.")
                break
        else:
            # TODO: 5. Process coins.
            paid_money = process_coin()
            # TODO: 6. Check transaction successful?
            if paid_money >= MENU[prompt]["cost"]:
                change = paid_money - MENU[prompt]["cost"]
                if change > 0:
                    print(f"Here is ${round(change, 2)} in change.")
                    print(f"Here is your {prompt} ☕️. Enjoy!")
                # TODO: 7. Make Coffee.
                for i in resources:
                    if not i == "money":
                        resources[i] -= MENU[prompt]["ingredients"][i]
                    else:
                        resources[i] += MENU[prompt]["cost"]
            elif paid_money == 0:
                continue
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("Wrong entry. Try again!!")