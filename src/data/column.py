import numpy as np
import matplotlib.pyplot as plt

with open("matrix.mat", "rb") as f:
    s = f.read()

m = np.fromstring(s)
m = m.reshape(450, 450)

while True:
    fig, (ax1, ax2) = plt.subplots(2, figsize=(20, 10))
    ax1.spy(m)
    l = np.linalg.cholesky(m)
    ax2.spy(l)
    plt.show()
    print(np.count_nonzero(l))
    sw = input()
    sw = sw.split(" ")
    sw1_start = int(sw[0])
    sw1_end = int(sw[1])
    sw2_start = int(sw[2])
    perm = np.arange(450)
    for i in range(0, sw1_end - sw1_start):
        perm[sw1_start + i] = sw2_start + i
        perm[sw2_start + i] = sw1_start + i
    m = m[perm][:,perm]
