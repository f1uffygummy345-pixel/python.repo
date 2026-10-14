print("Rocket Countdown")
starting_number = int(input("Enter a starting number: "))

while starting_number < 1:
    starting_number = int(input(f"Hey! Gotta be positive! {starting_number} ain't that! Enter a starting number: "))

counter = starting_number
 
while starting_number >= 1:
    print(starting_number)
    starting_number -= 1
    
print("Blast off")

