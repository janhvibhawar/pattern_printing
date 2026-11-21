print("Right-Aligned Triangle")
n = 5
for i in range(1, n + 1):  # Outer looop  for rows starting from 1 to 5 
    for j in range(n - i): # first inner loop for column for printing spaces in the start
        print(" ", end=" ") # printing spaces 
    for k in range(i): # second inner loop for printing stars same as number or rows 
        print("*", end=" ") 
    print()  # moving to next row
