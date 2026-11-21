print("Inverted Pyramid")
n = 5
for i in range(n, 0, -1):  # Outer loop for for number of rows and the number decreases by 1 for each row 
    for j in range(n - i): # first inner loop for number of columns for printing number of spaces n- i the number increases by 1 for each row as i increases
        print(" ", end=" ")
    for k in range(2 * i - 1):  # second inner loop for printing * here star decreases by 2 in each row 
        print("*", end=" ")
    print()  # moving to next row
