#2. create a file named leap_year.py in this folder. Write a program to
#determine if a user input year is a leap year. A year is a leap year if it is
#divisible by 4 but not by 100, or if it is divisible by 40

#year = int(input("Enter a year: "))

#if (year % 4 == 0 and year % 100 !=0)  or  year % 400 == 0:
   # print(f"Is {year} a leap year? True")
#else:
    #print(f"Is {year} a leap year? False")

#1 print
#if (year % 4 == 0 and year % 100 !=0)  or  year % 400 == 0:
  #  result = "True"
#else:
   # result ="False"

#print(f"Is {year} a leap year? {result}")

#no else
result = "False"
#if (year % 4 == 0 and year % 100 !=0)  or  year % 400 == 0:
   # result = "True"
#print(f"Is {year} a leap year? {result}")

#no if
#print(f"Is {year} a leap year? {(year % 4 == 0 and year % 100 !=0) or year % 400}")


month_number = int(input("Enter a month number (1-12): "))

print("Month is: ")
match month_number:
    case 1:
        print("January")
    case 1:
        print("February")
    case 1:
        print("March")
    case 1:
        print("April")
    case 1:
        print("May")
    case 1:
        print("June")
    case 1:
        print("July")
    case 1:
        print("August")
    case 1:
        print("September")
    case 1:
        print("October")

