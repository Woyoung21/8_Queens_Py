def check_queens_chessboard(x, y):
    # Loop over all pairs of queens
    for i in range(8):
        for j in range(i + 1, 8):
            # Check if queens share the same row, column, or diagonal
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return "YES"
    return "NO"

x = []
y = []

# Read in the 8 pairs of coordinates
for inputs in range(8):
    a_list = [int(s) for s in input().split()]  # Use list comprehension to parse input
    x.append(a_list[0])
    y.append(a_list[1])

# Print the result
print(check_queens_chessboard(x, y))
