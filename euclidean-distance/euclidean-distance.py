import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    sum = 0
    for i in range(len(x)):
        sum = sum + (x[i]-y[i])**2
    sum = sum**(0.5)
    return sum
    pass