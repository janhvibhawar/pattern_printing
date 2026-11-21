print("Butterfly Pattern")
n = 5

# Upper half
for i in range(1, n + 1):  # outer loop for rows in upper half here from 1 to 5
    for j in range(i):  # first inner loop prints left wing stars increases by 1 in each row
        print("*", end=" ")
    for j in range(2 * (n - i)):  # second inner loop prints middle gap spaces 2*(n-i) units decreases by 2 units each row
        print(" ", end=" ")
    for j in range(i):  # third inner loop prints right wing stars same count as left wing
        print("*", end=" ")
    print()  # moving to next row

# Lower half
for i in range(n - 1, 0, -1):  # outer loop for rows in lower half starts at n - 1 so the middle row doesn't repeat
    for j in range(i):  # first inner loop prints left wing stars decreases by 1 in each row
        print("*", end=" ")
    for j in range(2 * (n - i)):  # second inner loop prints middle gap spaces increases by 2 units as wings decreases
        print(" ", end=" ")
    for j in range(i):  # third inner loop prints right wing stars same count as left wing
        print("*", end=" ")
    print()  # moving to next row
