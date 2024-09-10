import numpy as np


def main():
    n_iter = 1000
    n_in = 0
    for i in range(1, n_iter + 1):
        x = np.random.rand()
        y = np.random.rand()
        if x**2 + y**2 <= 1:
            n_in += 1
        if i % 100 == 0:
            print("Iteration: ", i, "Pi/4: ", n_in / i)


if __name__ == "__main__":
    main()
