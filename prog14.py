# Multiplication of matrix using function

def matrix_multiply(A, B):
    a_row_count = len(A)
    a_col_count = len(A[0])
    b_row_count = len(B)
    b_col_count = len(B[0])

    # Initialize empty matrix
    result = [[0 for _ in range(b_col_count)] for _ in range(a_row_count)]
    if (a_col_count == b_row_count):
        for i in range(a_row_count):
            for j in range(b_col_count):
                for k in range(a_col_count):
                    result[i][j] += A[i][k] * B[k][j]
        return result
    else:
        print("Not defined")
        return


# Example matrices
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

print(matrix_multiply(A, B))
