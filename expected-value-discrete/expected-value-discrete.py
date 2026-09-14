import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    n = len(x);
    e = 0;
    for i in range(n):
        e = e + float(x[i]*p[i])
    return e;
    
    
    pass