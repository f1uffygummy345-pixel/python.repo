from datetime import datetime
#date as a string
my_birthday = "10/02/2008"

# read the string date into a datetime object
my_birthday_dateTime_object = datetime.strptime(my_birthday, "%m/%d/%Y")

print(my_birthday_dateTime_object)

# back to a string
my_birthday_string = my_birthday_dateTime_object.strftime("%m/%d/%Y")

print(my_birthday_string)
print(my_birthday_dateTime_object.strftime("%A"))