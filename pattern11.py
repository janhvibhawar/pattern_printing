print("Hollow right angled triangle")
n = 5
for i in range(n):  # Outer loop for number of rows here from 0 to 4
    for j in range(i + 1): # inner loop for number of columns from 0 till i so each row increases by 1 column like right angle triangle
        if j == 0 or j == i or i == n - 1:   # condition to check if current position is left border, bottom row or diagonal 
            print("*", end=" ")  # if condition is true then print *
        else:
            print(" ", end=" ")  # if condition is false then print space
    print() # Moving to next row
