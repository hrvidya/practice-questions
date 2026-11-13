r, c = map(int, input("Enter rows and columns: ").split())

if r <= 0 or c <= 0:
    print("Invalid Matrix")
    exit()

matrix = []

print("Enter matrix elements:")

for i in range(r):
    row = list(map(int, input().split()))

    if len(row) != c:
        print("Invalid row size")
        exit()

    matrix.append(row)

# Print Matrix
print("\nMatrix:")

for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=" ")
    print()

# Print Rows Separately
print("\nRows:")

for i in range(r):
    print(f"Row {i}:", matrix[i])

# Print Columns Separately
print("\nColumns:")

for j in range(c):

    print(f"Column {j}:", end=" ")

    for i in range(r):
        print(matrix[i][j], end=" ")

    print()

# Primary Diagonal Sum
primary_sum = 0

for i in range(min(r, c)):
    primary_sum += matrix[i][i]

print("\nPrimary Diagonal Sum:", primary_sum)

# Secondary Diagonal Sum
secondary_sum = 0

for i in range(min(r, c)):
    secondary_sum += matrix[i][c - 1 - i]

print("Secondary Diagonal Sum:", secondary_sum)