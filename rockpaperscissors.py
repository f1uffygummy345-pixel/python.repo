import random

# Generate a random number for the computer
computer = random.randint(0, 2)

# Ask the user for their choice
user = int(input("Enter a number (0-2): "))

# Display choices
choices = ["scissor", "rock", "paper"]

print("You chose:", choices[user])
print("Computer chose:", choices[computer])

# Determine the winner
if user == computer:
    print("It is a draw!")
elif (user == 0 and computer == 2) or \
     (user == 1 and computer == 0) or \
     (user == 2 and computer == 1):
    print("You win!")
else:
    print("You lose!")
