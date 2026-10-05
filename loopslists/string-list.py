name = "Emma"
name = ["E", "m", "m", "a"]

for character in name:
    print(character)
    
name = input("Enter your name: ")
character = input("Enter a character: ")

if character in name:
    print(f"{character} is in {name}")
else:
    print(f"{character} is not in {name}")