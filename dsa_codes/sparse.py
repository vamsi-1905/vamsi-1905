
l = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))


print("Enter matrix elements row-wise:")
sparseMatrix = []
for i in range(l):
    row = list(map(int, input().split()))
    if len(row) != m:
        print("Please enter exactly", m, "elements.")
        exit()
    sparseMatrix.append(row)


size = 0
for i in range(l):
    for j in range(m):
        if sparseMatrix[i][j] != 0:
            size += 1


compactMatrix = [[0] * size for _ in range(3)]

k = 0
for i in range(l):
    for j in range(m):
        if sparseMatrix[i][j] != 0:
            compactMatrix[0][k] = i
            compactMatrix[1][k] = j
            compactMatrix[2][k] = sparseMatrix[i][j]
            k += 1



print("\nSparse Matrix Representation (row, col, value):")
for row in compactMatrix:
    print(row)

k = 0
for i in range(l):
    for j in range(m):
        if sparseMatrix[i][j] != 0:
            compactMatrix[0][k] = j
            compactMatrix[1][k] = i
            compactMatrix[2][k] = sparseMatrix[i][j]
            k += 1

print("transpose of matrix:")
for row in compactMatrix:
    print(row)

