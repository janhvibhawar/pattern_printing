print("Increasing Number Triagle")
n = 5
for i in range(1, n + 1):  # Outer loop for rows from 1 to 5 here 
    for j in range(1, i + 1): # inner loop for columns starting from 1 till i
        print(j, end=" ")    # here we are printing j it is column number and then space
    print()  # moving to next row