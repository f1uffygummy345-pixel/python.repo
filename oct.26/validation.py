def get_valid_quantity():
    while True:
        try:
            quantity = int(input("Enter a quantity: "))
        except ValueError:
            print("Please enter a whole number")
            continue
        return quantity
    
 