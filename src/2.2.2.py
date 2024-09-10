import numpy as np


def main():
    n_iter = 1000
    n_in = 0
    for k in range(1, n_iter + 1):
        x_k = np.random.rand()
        f_x = np.sqrt(1 - x_k**2)
        n_in += f_x
        if k % 100 == 0:
            print("Iteration: ", k, "Pi/4: ", n_in / k)


if __name__ == "__main__":
    main()
