import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """
    # Your code here
    B = A.T @ A
    phi = np.pi / 4 if B[0][0] == B[1][1] else 0.5 * np.atan(2 * B[0][1] / (B[0][0] - B[1][1]))

    R = np.array([[np.cos(phi), -np.sin(phi)], [np.sin(phi), np.cos(phi)]])
    D = R.T @ B @ R
    S = np.sqrt(np.diag(D))
    U = A @ R @ np.diag(1 / S)

    order = np.argsort(S)[::-1]
    S = S[order]
    R = R[:, order]

    return U, S, R.T