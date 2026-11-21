print("Hollow Square")
n = 5
for i in range(n):  # Outer loop for number of rows here from 0 to 4
    for j in range(n):  # inner loop for number of columns here from 0 to 4 same as number of rows
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:  # this conditions check if the current position is only on border that is first row, last row , first column, last column
            print("*", end=" ") # if condition is true then only print star
        else:
            print(" ", end=" ")  # else we will print space
    print() # moving to next row
 