import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    x1 = np.asarray(x,dtype=float)
    y1 = np.asarray(y,dtype=float)
    s = abs(np.array(y1-x1))
    s = np.sum(s)
    return s
    pass