import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    sum = 0.0
    for i in range(len(x)):
        sum = sum+(x[i]*y[i])
    return sum
    pass