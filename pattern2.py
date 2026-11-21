print("Right angled triangle")
n = 5
for i in range(1, n + 1):  # Outer loop for rows 
    for j in range(i): # inner loop as number of star printing on each row is same as number of rows so this loop will go till i
        print("*", end=" ")     # printing * and space 
    print()  # for moving to next line or row

    