#A function is a block of code that performs a task, define it once and call it when needed
#Why?
#code reuse 
#maintainable
#Simple testing
#large problem into smaller problems

#Ask for a quantity and return a valid quantity(int)
def get_valid_quantity():
    while True:
        try:
            valid_quantity = int(input("Enter a quantity: "))
        except ValueError:
            print("Please enter a whole number")
            continue
            return valid_quantity

def display_welcome():
    print("Welcome to the Snack Shack!")
    print("Most snacks are $4.00")

def calculate_total(quantity, unit_price = 4.00):
    total = quantity * unit_price
    return total

def display_recipt(item_name,quantity, total):
    print(f"Snack: {item_name}")
    print(f"Quantity: {quantity}")
    print(f"Total: ${total:.2f}")
    
    
UNIT_PRICE = 3.00

display_welcome()
item_name = input("Snack name: ")
quantity = int(input("How many: "))
#total = calculate_total(quantity, UNIT_PRICE) # overriding the default
#total = calculate_total(quantity) # using the default
total = calculate_total(quantity = quantity, unit_price = UNIT_PRICE) #using keyword arguments
display_recipt(item_name, quantity, total)