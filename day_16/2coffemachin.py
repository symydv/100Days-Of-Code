#by me

from menu import Menu,MenuItem
from coffemaker import CoffeeMaker
from moneymachin import MoneyMachine


coffee=Menu()
make=CoffeeMaker()
money=MoneyMachine()

on=True
while on:

    print("which coffee do you want",coffee.get_items())
    order=coffee.find_drink(input(""))

    # x=MenuItem(name=order,cost=order.cost,water=order.ingredients["water"],milk=order.ingredients["milk"],coffee=order.ingredients["coffee"])


    if make.is_resource_sufficient(order):
        if money.make_payment(order.cost):
            make.make_coffee(order)
        else:
            print("not sufficient money")
    else:
        print("not sufficient ingrideants")


    next=input("type on to give another order,off to close machine or report to get info on remaining resources:")
    if next=="on":
        on=True
    elif next=="off":
        on=False
    elif next=="report":
        make.report()
        money.report()
        aab=input("type on to give another order,off to close machine:")
        if aab=="on":
            on=True
        elif aab=="off":
            on=False



###############_BY MAAM_#############
            
# from menu import Menu
# from coffemaker import CoffeeMaker
# from moneymachin import MoneyMachine

# money_machine = MoneyMachine()
# coffee_maker = CoffeeMaker()
# menu = Menu()

# is_on = True

# while is_on:
#     options = menu.get_items()
#     choice = input(f"What would you like? ({options}): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink = menu.find_drink(choice)
        
#         if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
#           coffee_maker.make_coffee(drink)
