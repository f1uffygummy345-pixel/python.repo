bands = ["Abba", "Journey", "Max Rebo", "Styx", "The Beetles"]
#for loops allow us to look at each element in a list

for band in bands:
    print(f"{band} is a great band")
# loops through entire list
# each value in the list populates band

fruits = ["Blueberry", "Durian", "Strawberry"]
#for index,  fruit in enumerate(fruits):
    #print(f"{fruit} is at index {index}")
    

#Start list at 1
#for index,  fruit in enumerate(fruits):
    #print(f"{fruit} is at index {index + 1}")
    
#or
for index, fruit in enumerate(fruits, start = 1):
    print(f"{fruit} is at index {index}")
    
#create a list that displays a menu
#only use 1 print statement
#1. Add
#2. Edit
#3. Delete
#4. Exit

menu = ["Add", "Edit", "Delete", "Exit"]
for index, menu in enumerate(menu, start = 1):
    print(f"{index}. {menu}")