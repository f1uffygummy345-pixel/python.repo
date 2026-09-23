#sorting
numbers = [42,7,19,100,3]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

#add a single value to a list
numbers.append(37)
print(numbers)
#add at an index
numbers.insert(2,84)
print(numbers)

#append a list to a list
numbers.extend([1,3,5,7,9])
print(numbers)

#insert a list at an index
numbers [5:5] = [2,4,6,8,10]
print(numbers)

#removing values
#pop(index) - removes and returns the value
pets = ["cat", "dog","lizards","birds","hamster"]
removed_value = pets.pop(3)
print(removed_value)
print(pets)

#del
del pets[1]
print(pets)

#searching
cities = ["Edmonton", "Calgary", "Toronto", "Red Deer"]
print(f"Is Calgary in the list? {"Calgary" in cities}")

check_city = input("Enter a city: ")
result = check_city in cities#True or False
if result:
    print(f"{check_city} is in the list")
else:
    print(f"{check_city} is not in the list")

#index of a value
print(f"The index of Red Deer is: {cities.index("Red Deer")}")

cities[cities.index("Red Deer")] = "Red Deeer"
print((cities))

#how many times is a value in the list?
cities = ["Edmonton", "Calgary", "Toronto", "Red Deer", "Edmonton"]
print(f"Edmonton is in the list {cities.count("Edmonton")} times")

#empty list
names = []
print(names)
names = input("Enter a name: ")
names.append(names)
names = input("Enter a name: ")
names.append(names)
print(names)