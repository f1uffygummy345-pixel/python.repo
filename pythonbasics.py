print("Intro to Python")
# Comment - does not execute
# Describes your code for others to read

# Multi lines
# comment Use
# ctrl /

#Case Sensitive
# Extra spaces in your code do not usually matter
# Strings can use "" or ''

#print('Let's go crazy')
print ("Hello")
print("Let's go crazy")

# Escape character/sequences - provide a way to perform an action IN a string:

print('It\'s a "groovy" day!')
print("It's a \"groovy\" day!")
print("Hello\n World") #New line
print("Name:\tEmma") # Tab

print("To go to a new line in a string use \\n")

# Variables
# a named box or container that holds a value
# value can change
# use snake_case for the names
# names can only contain letters, numbers, and underscores. Cannot start with a number.
# not explicitly declared in python

# datatypes
first_name = "Emma" #string
age = 18 #integer
price = 12.23 # float
is_valid = True #boolean (True/False)

# String formatting
# String concatenation
print("Your name is " + first_name + " and you are " + str(age) + " years young.")


#OR 
print("Your name is",first_name,"and you are",age,"years young.")

#OR (Best Way)
print(f"Your name is {first_name} and you are {age} years young.")

#Constants
#like a variable that does not change
# Use SCREAMING_SNAKE_CASE
GST_RATE = 0.05
subtotal = 100
total = subtotal * 0.05
total = subtotal * GST_RATE

# Input from user
# Input always returns a string
name = input("Enter your name: ")
print(f"Welcome {name}")
print(f"Welcome {name}")

#add numbers and display the sum
number1 = input("Enter number 1: ")
number2 = input("Enter number 2: ")

sum = int(number1) + int(number2) # pyright: ignore[reportUndefinedVariable]
print(f"{number1} + {number2} = {sum}")
#OR
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

sum = number1 + number2
print(f"{number1} + {number2} = {sum}")