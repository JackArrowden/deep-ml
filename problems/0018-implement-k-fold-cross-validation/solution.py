import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    # Your code here
    n, step = n_samples, n_samples // k
    ids = np.arange(n)
    if shuffle:
        np.random.shuffle(ids)
    ids = ids.tolist()
    
    k_folds = [ids[: step + n % k]] \
        + [ids[step * i + n % k : step * (i + 1) + n % k] \
            for i in range(1, k)]

    result = []
    for i in range(k):
        train = [id for j in range(k) if j != i for id in k_folds[j]]
        result.append((train, k_folds[i]))

    return result