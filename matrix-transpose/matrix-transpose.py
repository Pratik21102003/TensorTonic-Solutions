import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    rows=len(A)
    col=len(A[0])
    transpose=[]
    for j in range(col):
        row=[]
        for i in range(rows):
             row.append(A[i][j])
        transpose.append(row)
    return np.array(transpose)
    pass
