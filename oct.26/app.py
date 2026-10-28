from validation import get_valid_quantity
from pricing import calculate_total
from display import display_welcome, display_recipt


def main():
    UNIT_PRICE = 3.00
    display_welcome()
    item_name = input("Snack name: ")
    quantity = int(input("How many: "))
    quantity = get_valid_quantity()
    #total = calculate_total(quantity, UNIT_PRICE) # overriding the default
    #total = calculate_total(quantity) # using the default
    total = calculate_total(quantity = quantity, unit_price = UNIT_PRICE) #using keyword arguments
    display_recipt(item_name, quantity, total)

#If running the app from this module (__name__ == __main__)
#If importing and running __name__ is the name of the module being imported
if __name__ == "__main__":
    main()