from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine2 = MoneyMachine()
coffee_maker2 = CoffeeMaker()
menu = Menu()

is_on =True


while is_on:
    options = menu.get_items()
    choice = input(f"What would you Like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker2.report()
        money_machine2.report()

    else:
        drink = menu.find_drink(choice)
        if coffee_maker2.is_resource_sufficient(drink) and money_machine2.make_payment(drink.cost):
            coffee_maker2.make_coffee(drink)
