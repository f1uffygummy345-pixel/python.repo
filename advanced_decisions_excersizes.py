#2. create a file named leap_year.py in this folder. Write a program to
#determine if a user input year is a leap year. A year is a leap year if it is
#divisible by 4 but not by 100, or if it is divisible by 40

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 !=0)  or  year % 400 == 0:
    print(f"Is {year} a leap year? True")
else:
    print(f"Is {year} a leap year? False")
    
