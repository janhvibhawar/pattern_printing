print("Star Pyramid")
n = 5
for i in range(1, n + 1): # Outer loop for number of rows here it is from 1 to 5
    for j in range(n - i):  # first inner loop for number of columns for printing spaces  , also n - i formula decreases a number in each iteration so in first it will print 4 spaces then 3 then 2 ans so on
        print(" ", end=" ")
    for k in range(2 * i - 1):  # second inner loop for printing starts as * is increasing by 2 in each row so we multiply number of row by 2 and subtract by 1 so we get a number which increases by 2 for each row
        print("*", end=" ")  # printing star and then space 
    print()  # moving to next row
