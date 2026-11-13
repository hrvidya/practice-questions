r = int(input())
c = int(input())

matrix = []

for i in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)

for j in range(c):

    for i in range(r):

        print(matrix[i][j], end=" ")

    print()