#ternary condition
#if/else

grade = int(input("Enter a grade: "))

if grade >= 50:
    print("Pass")
else:
    print("Fail")

#ternary
#value_if_true if condition else value_if_false
result = "pass" if grade >= 50 else "Fail"
print(result)
print("Pass" if grade >= 50 else "Fail")
print()
