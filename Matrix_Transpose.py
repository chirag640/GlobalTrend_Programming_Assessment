def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = transpose_matrix(matrix)
for row in transposed:
    print(row)
