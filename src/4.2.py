import numpy as np


def S(x):
    return 0.5 * x * x


def main():
    n_iter = 100
    step_size = 0.5
    x = 0
    naccept = 0
    for iter in range(1, n_iter + 1):
        backup_x = x
        action_init = S(x)

        dx = np.random.uniform(-step_size, step_size)
        x = x + dx

        action_fin = S(x)

        metropolis = np.random.rand()
        if np.exp(action_init - action_fin) > metropolis:
            naccept += 1
        else:
            x = backup_x
