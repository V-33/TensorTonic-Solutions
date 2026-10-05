import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    arr = np.asarray(X, dtype=float)
    
    mean = np.mean(arr, axis=axis, keepdims=True)
    std = np.std(arr, axis=axis, keepdims=True, ddof=0)
    
    mask = std <= eps
    
    std_safe = np.where(mask, 1.0, std)
    z = (arr - mean) / std_safe
    
    return np.where(mask, 0.0, z)