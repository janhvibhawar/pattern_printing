print("Diamond")
n = 5

# Upper half
for i in range(1, n + 1):  # Outer loop for number of rows in upper half just like start pyramid
    for j in range(n - i):  # first inner loop of upper half for printing leading spaces before star in each row spaces decrease by 1 unit for each row
        print(" ", end=" ")
    
    for k in range(2 * i - 1):  # second inner loop of upper half for printing odd number of stars (2*i - 1) after spaces end=" " keeps stars spaced on same line
        print("*", end=" ")
    print()  # moving to next row

# Lower half 
for i in range(n - 1, 0, -1):  # Outer loop for number of rows in lower half just like inverted star pyramid starts at n - 1 so middle row doesn't repeat
    for j in range(n - i):  # first inner loop of lower half for printing leading spaces before star in each row; spaces increase by 1 unit for each row
        print(" ", end=" ")
    for k in range(2 * i - 1):  # second inner loop of lower half for printing decreasing odd number of stars 2*i - 1 after spaces
        print("*", end=" ")
    print()  # moving to next row
