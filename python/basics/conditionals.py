# Types of conditionals in Python:
# 1. if statement
# 2. if-else statement
# 3. if-elif-else statement
# 4. nested if statement
# 5. Conditional expressions (ternary operator)
# 6. match-case statement (Python 3.10 and above)

# 1. if statement
x = 10
if x > 5:
    print("x is greater than 5")

# 2. if-else statement
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

# 3. if-elif-else statement
x = 10
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")

# 4. nested if statement
x = 10
y = 5
if x > 5:
    if y > 2:
        print("Both conditions are true")
    else:
        print("x is greater than 5 but y is not greater than 2")
else:
    print("x is not greater than 5")

# 5. Conditional expressions (ternary operator)
x = 10
result = "x is greater than 5" if x > 5 else "x is less than or equal to 5"
print(result)

# 6. match-case statement (Python 3.10 and above)
x = 10
match x:
    case 5:
        print("x is 5")
    case 10:
        print("x is 10")
    case _: # the underscore (_) is a wildcard that matches any value and acts as a default case
        print("x is neither 5 nor 10")

