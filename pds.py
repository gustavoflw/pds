import numpy as np

# Função degrau unitário
def u(n):
    return 1 * (n >= 0)

# Função impulso
def delta(n):
    return 1 * (n == 0)

# Mean square error
def mse(r, s):
    return np.mean(np.abs(r-s) ** 2)

# 
def eqdif(b, a, x):
    y = np.zeros_like(x)

    for n in range(len(y)):
        for k in range(1, len(a)):
            if n - k >= 0:
                y[n] -= a[k] * y[n-k]
        for k in range(len(b)):
            if n - k >= 0:
                y[n] += b[k]*x[n-k]

    return y