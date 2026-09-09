import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    ar = np.asarray(A)
    r = len(np.array(A))
    c = len(np.array(A)[0])

    y = np.zeros((c,r))
    for i in range(r):
        for j in range(c):
            y[j,i] = ar[i,j]
    return y
    pass
