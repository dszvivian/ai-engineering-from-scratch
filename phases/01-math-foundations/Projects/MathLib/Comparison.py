import numpy as np
import torch

from Matrices import Matrix
from Timer import Timer

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

def create_matrix(n, seed=42):
    np.random.seed(seed)

    i = np.arange(n).reshape(-1, 1)
    j = np.arange(n).reshape(1, -1)

    # Structured + non-trivial matrix
    mat = (
        np.sin(i * 0.1) +
        np.cos(j * 0.1) +
        (i * j) / (n * n) +
        np.random.rand(n, n) * 0.01
    )

    return mat

N = 1024
mata = create_matrix(N)
matb = create_matrix(N, seed=42)


ma_list = Matrix(mata.tolist())
mb_list = Matrix(matb.tolist())

with Timer("My MathLib"):
    res1 = ma_list @ mb_list

with Timer("Numpy"):
    print(DEVICE)
    res2 = mata @ matb

ma_t = torch.tensor(mata, dtype=torch.float32, device=DEVICE)
mb_t = torch.tensor(matb, dtype=torch.float32, device=DEVICE)

with Timer("Pytorch"):
    res3 = ma_t @ mb_t



