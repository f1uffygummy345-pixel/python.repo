#We want trap exceptions
#keep program running AND give nice error messages


#Use try/except
#sum = 0 
#count = 0

#while True:
  #  try:
  #      number = int(input("Enter an integer number: "))
  #  except ValueError as error_message:
  #      print(f"Invalid Input. Must be an integer. Error message: {error_message}")
  #      continue #loop until valid input
  #  if number == -1:
  #      break
 #   sum += number
  #  count += 1

#try:
   # average = sum/count
  #  print(f"The average is {average}")
#except ZeroDivisionError: #don't want the error message. Optional.
    #print("No numbers were entered.")


sum = 0 
count = 0

while True:
    try:
        number = int(input("Enter an integer number: "))
    except ValueError as error_message:
        print(f"Invalid Input. Must be an integer. Error message: {error_message}")
        continue #loop until valid input
    if number == -1:
        break
    sum += number
    count += 1

try:
    average = sum/count
    print(f"The average is {average}")
except ZeroDivisionError: #don't want the error message. Optional.
    print("No numbers were entered.")
#finally always executes
finally:
    print("Always executes")
    
#multiple exceptions for one try
#try:
   # number = int(input("Enter an integer: "))
    #result = 100/number
#except ValueError:
 #   print("Invalid input. Must be an integer")
#except ZeroDivisionError:
#    print("Cannot have a zero denominator")
#except:
  #  print("Unknown Error")
    
sum = 0 
count = 0

while True:
    try:
        number = int(input("Enter an integer number: "))
        if number < -1:
            raise ValueError ("Number must not be negative")
    except ValueError as error_message:
        print(f"Invalid Input. Must be an integer. Error message: {error_message}")
        continue #loop until valid input
    if number == -1:
        break
    sum += number
    count += 1

try:
    average = sum/count
    print(f"The average is {average}")
except ZeroDivisionError: #don't want the error message. Optional.
    print("No numbers were entered.")