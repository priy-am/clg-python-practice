# 34. WAP for multiplication of 3*3 Matrices 
def matricesMultiplication(A, B):
    result = [[0, 0, 0] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += A[i][k] * B[k][j]
    return result

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = matricesMultiplication(A, B)
print("Resultant Matrix:")
for row in result:
    print(row)

# 35. WAP to enter elements of 3*3 matrix on runtime
matrix = []
for _ in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)


print("The 3×3 Matrix is:")
for row in matrix:
    print(row)