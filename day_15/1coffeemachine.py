from menu import MENU, resources
money = 0
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

es = MENU["espresso"]
es_ing = es["ingredients"]

lat = MENU["latte"]
lat_ing = lat["ingredients"]

cap = MENU["cappuccino"]
cap_ing = cap["ingredients"]



def check_resources():
    if want == "espresso":
        if es_ing["water"] <= water and coffee >= es_ing["coffee"]:
            return True
        else:
            print("insuficient resources")
        
        
    elif want == "latte":
        if lat_ing["water"] <= water and coffee >= lat_ing ["coffee"] and milk >= lat_ing["milk"]:
            return True
        else:
            print("insuficient resources")
        
    elif want == "cappuccino":
        if cap_ing["water"] <= water and coffee >= cap_ing["coffee"] and milk >= cap_ing["milk"]:
            return True
        else:
            print("insuficient resources")
        
def porcess_coins():
    global coins
    quarter = float(input("inser quarters: "))
    dimes = float(input("inser dimes: "))
    nickles = float(input("inser nickles: "))
    pennies = float(input("inser pennies: "))
    coins = quarter*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    if want == "espresso":
        if coins >= es["cost"]:
            return True
        else:
            print("insufficient coins, coins has returned")
        
    if want == "latte":
        if coins >= lat["cost"]:
            return True
        else:
            print("insufficient coins, coins has returned")
        
    if want == "cappuccino":
        if coins >= cap["cost"]:
            return True
        else:
            print("insufficient coins, coins has returned")
    
def transaction():
    global money,water,coffee,milk,change,coins
    if want == "espresso":
        change = coins - es["cost"]
        money += es["cost"]
        water -= es_ing["water"]
        coffee -= es_ing["coffee"]
        if coins >= es["cost"]:
            print(f"here is your change of ${change}")
            print("and your ordered espresso")

    elif want == "latte":
        change = coins - lat["cost"]
        money += lat["cost"]
        water -= lat_ing["water"]
        coffee -= lat_ing["coffee"]
        milk -= lat_ing["milk"]
        if coins >= lat["cost"]:               
            print(f"here is your change of ${change}")
            print("and your ordered latte")

    elif want == "cappuccino":
        change = coins - cap["cost"]
        money += cap["cost"]
        water -= cap_ing["water"]
        coffee -= cap_ing["coffee"]
        milk -= cap_ing["milk"]
        if coins >= cap["cost"]:
            print(f"here is your change of ${change}")
            print("and your ordered cappuccino")
 
want = 1
while want != "stop":
    want = input("what would you like? (espresso/latte/cappuccino): ")

    if want == "report":
        print(f"water: {water}ml\nmilk: {milk}ml\ncoffee: {coffee}gm\nmoney: ${money}")
    if check_resources() == True:
        if porcess_coins() == True:
            transaction()

