#ternary condition
#if/else

grade = int(input("Enter a grade: "))

if grade >= 50:
    print("Pass")
else:
    print("Fail")

#ternary
#value_if_true if condition else value_if_false
result = "pass" if grade >= 50 else "Fail"
print(result)
print("Pass" if grade >= 50 else "Fail")
print()

#even or odd
number = int(input("Enter a number: "))
result = "Even" if number % 2 == 0 else "Odd"
print(result)



#ask for two numbers and print the largest number
number1 = (number1 if number1 > number2 else number2)
print(largest)

print(number1 if number1 > number2 else number2)