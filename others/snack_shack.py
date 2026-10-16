#A function is a block of code that performs a task, define it once and call it when needed
#Why?
#code reuse 
#maintainable
#Simple testing
#large problem into smaller problems


print("Welcome to the Snack Shack!")
print("Snacks are all $4.00")
item_name = input("Snack name: ")
quantity = int(input("How many: "))
total = quantity * 4
print(f"Snack: {item_name}")
print(f"Quantity: {quantity}")
print(f"Total: ${total:.2f}")
