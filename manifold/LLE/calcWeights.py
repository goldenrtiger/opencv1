#计算近邻的距离，并按小到大排列
#indices len(X)*n_neighbors的向量，每一行表示距离本样本距离由小到大的样本的index
#distances len(X)*n_neighbors的向量，每一行表示最邻近的n_neighbors个样本距离本样本点的距离

import numpy as np
from sklearn.neighbors import NearestNeighbors
from scipy.linalg import eigh, svd, qr, solve
from scipy.sparse import eye, csr_matrix

def barycenter_weights(X, Z, reg=1e-3):
    """Compute barycenter weights of X from Y along the first axis

    We estimate the weights to assign to each point in Y[i] to recover
    the point X[i]. The barycenter weights sum to 1.

    Parameters
    ----------
    X : array-like, shape (n_samples, n_dim)

    Z : array-like, shape (n_samples, n_neighbors, n_dim)

    reg : float, optional
        amount of regularization to add for the problem to be
        well-posed in the case of n_neighbors > n_dim

    Returns
    -------
    B : array-like, shape (n_samples, n_neighbors)

    Notes
    -----
    See developers note for more information.
    """
    # X = check_array(X, dtype=FLOAT_DTYPES)
    # Z = check_array(Z, dtype=FLOAT_DTYPES, allow_nd=True)

    n_samples, n_neighbors = X.shape[0], Z.shape[1]
    B = np.empty((n_samples, n_neighbors), dtype=X.dtype)
    v = np.ones(n_neighbors, dtype=X.dtype)

    # this might raise a LinalgError if G is singular and has trace
    # zero
    for i, A in enumerate(Z.transpose(0, 2, 1)):
        C = A.T - X[i]  # broadcasting
        G = np.dot(C, C.T)
        trace = np.trace(G)
        if trace > 0:
            R = reg * trace
        else:
            R = reg
        G.flat[::Z.shape[1] + 1] += R
        w = solve(G, v, sym_pos=True)
        B[i, :] = w / np.sum(w)
    return B



# samples = [[0,0,2], [1,0,0], [0,0,1]]
samples = np.array([[1.0, 1.0], [2.0, 1.0], [3.0, 2.0], [1.0, 1.0], [2.0, 1.0], [3.0, 2.0]])
neigh = NearestNeighbors(4, 0.4)
nbrs = neigh.fit(samples)
X = nbrs._fit_X #整理samples
# n_samples = nbrs.n_samples_fit_
n_samples = samples.shape[0]
ind = neigh.kneighbors(samples, return_distance=False)[:,1:]
data = barycenter_weights(samples, samples[ind])
indptr = np.arange(0, n_samples * 3 + 1, 3)
res = csr_matrix((data.ravel(), ind.ravel(), indptr), shape=(n_samples, n_samples))
print(res)

# distance, indices = nbrs.kneighbors(samples)
# print(distance)
# print(indices)
