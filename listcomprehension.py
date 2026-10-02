# given a list [2,4,6,8], use loop to create a new list of each of these values doubled

numbers = [2,4,6,8]

doubled = []

for number in numbers:
    doubled.append(number * 2)
print(doubled)
# list comprehension
numbers = [2,4,6,8]
doubled = [number * 2 for number in numbers]
print(doubled)

names = ["Bart", "Homer", "Marge"]
upper_case_names = [name.upper() for name in names]
print(upper_case_names)

#if
#Create a new list of only numbers that are >10
#without list comprehension AND with
numbers = [3,12,5,46,20,4]
large_numbers = []
for number in numbers:
    if number > 10:
       large_numbers.append(number)
print(large_numbers)

#if within list comprehension
numbers = [3,12,5,46,20,4]
large_numbers = [number for number in numbers if number > 10]
print(large_numbers)