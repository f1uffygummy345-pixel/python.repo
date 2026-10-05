#a list is a collection of values
#Each value in a list is stored in an index
#Each element is accessed by an index (starts at 0)
#can hold different data types in the same list

colors = ["red", "blue", "green", "yellow"]
print(colors)

#access an element
print(colors[1])

#from end of the list
print(colors[-2])

#changing a value
colors [3] = "purple"

#slicing
#get values from a range in the list
letters = ["a","b", "c","d","e"]
print(f"First three letters: {letters[0:3]}")
#lower boundary is inclusiv, the upper boundary is exclusive
#starting from start of list. omit the starting index
print(f"First three letters: {letters[:3]}")
print(f"middle letters: {letters[1:3]}")
#from the end
print(f"Last three letters: {letters[-3:]}")

#length of a list (number of elements)
print(len(letters))

#accessing a list outside its boundaries
print(letters[54])