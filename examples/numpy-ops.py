import numpy as np
import time
import random
def f_to_c(temp_f):
    return (temp_f - 32)*(5.0/9)

if __name__ == "__main__":
    N = 5000000

    highs_f = random.sample(range(50, 10*N), N)
    # Vanilla Python
    #highs_f = [68, 70, 75, 82, 80, 84]
    start_vanilla = time.time()
    highs_c = [f_to_c(t) for t in highs_f]
    #print(np.mean(highs_c))
    end_vanilla = time.time()

    # NumPy
    np_highs_f = np.array(highs_f)
    start_numpy = time.time()
    np_highs_c = f_to_c(np_highs_f)
    #print(np.mean(np_highs_c))
    end_numpy = time.time()

    print(f"Time for vanilla: {end_vanilla - start_vanilla}")

    print(f"Time for NumPy: {end_numpy - start_numpy}")

    print(f"Speed-up: {(end_vanilla - start_vanilla)/(end_numpy - start_numpy)}")

    np.linspace