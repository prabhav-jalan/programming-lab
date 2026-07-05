# python has only two loops:
# 1: for loop
# 2: while loop

# 1: for loop
for i in range(5):
    print(i)

arr = [1, 2, 3, 4, 5]
for i in arr:
    print(i)

# 2: while loop
i = 0
while i < 5:
    print(i)
    i += 1

# Loop control statements in Python:
# 1: break statement: used to exit the loop prematurely when a certain condition is met
for i in range(5):
    if i == 3:
        break
    print(i)

# 2: continue statement: used to skip the current iteration and move on to the next iteration
for i in range(5):
    if i == 3:
        continue
    print(i)

# 3: pass statement: used as a placeholder when a statement is required syntactically 
#                    but code is yet to be implemented
for i in range(5):
    if i == 3:
        pass
    else:
        print(i)

# 4: else statement: runs only if the loop finishes normally without encountering a 
#                    break statement or unhandled exception.
for i in range(5):
    print(i)
else:
    print("Loop is over")   


