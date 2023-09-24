import numpy as np

# Definícia matice A
A = np.array([[1, 2],
              [3, 4]])

# Definícia matice B
B = np.array([[5, 6],
              [7, 8]])

# Násobenie matíc A a B
C = np.dot(A, B)

# Výpis výslednej matice C
print("Matica C:")
print(C)

def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        raise ValueError("Počet stĺpcov matice A musí byť rovnaký ako počet riadkov matice B.")

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Definícia matíc A a B
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

# Násobenie matíc A a B
C = multiply_matrices(A, B)

# Výpis výslednej matice C
for row in C:
    print(row)
