lower = int(input("Enter a number: "))
upper = int(input("Enter a number: "))

my_square = int(input("Enter a number to sum the squares: "))

sum = 0

if lower > upper:
    print("Invalid Range")
else:
    for number in range(lower, upper + 1):
        sum += number ** 2
        
        
    print(f"The sum of the squares is: {sum}")



#Use list comprehension to create a list of squares from 1 to my_number

squares = [number ** 2 for number in range(1,my_square + 1)]
print(squares)

