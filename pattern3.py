print("Inverted right angled triangle")
n = 5
for i in range(n, 0, -1):  #Outer loop for number of rows  here it is starting from 5 to 1 and -1 represent it is decreasing by 1 for next row
    for j in range(i):        # inner loop till i as i start from n it will keep n stars in first row 
        print("*", end=" ")   # printing * and space
    print()    # Moving to for next line
