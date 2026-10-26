def get_valid_quantity():
    while True:
        try:
            valid_quantity = int(input("Enter a quantity: "))
        except ValueError:
            print("Please enter a whole number")
            continue
        return valid_quantity