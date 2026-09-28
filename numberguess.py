import random
random_numbers = [random.randint(1,10), random.randint(1,10), random.randint(1,10)]

guess =  int(input("Enter a number in the list: "))

if guess in random_numbers:
    print("You win!")
else:
    print("You lose!")
    
print(f"The numbers were: {random_numbers}")