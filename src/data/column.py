import numpy as np
import matplotlib.pyplot as plt

with open("matrix.mat", "rb") as f:
    s = f.read()

m = np.fromstring(s)
m = m.reshape(450, 450)

perm = np.arange(450)
for i in range(12):
    for j in range(6):
        perm[8 * i + j] = 6 * i + j
    perm[8 * i + 6] = 78 + 2 * i
    perm[8 * i + 7] = 78 + 2 * i + 1
for j in range(6):
    perm[8 * 12 + j] = 6 * 12 + j

for i in range(12):
    for j in range(3):
        perm[152 + 19 * i + j] = 152 + 3 * i + j
    for j in range(6):
        perm[152 + 19 * i + 3 + 2 * j] = 152 + 128 + 6 * i + j
        perm[152 + 19 * i + 3 + 2 * j + 1] = 152 + 128 + 85 + 6 * i + j
    for j in range(4):
        perm[152 + 19 * i + 15 + j] = 152 + 36 + 4 * i + j
for i in range(6):
    perm[152 + 19 * 12 + 2 * i] = 152 + 128 + 12 * 6 + i
    perm[152 + 19 * 12 + 2 * i + 1] = 152 + 128 + 85 + 12 * 6 + i
for i in range(44):
    perm[152 + 19 * 12 + 12 + i] = 152 + 36 + 48 + i
for i in range(7):
    perm[152 + 19 * 12 + 12 + 44 + 2 * i] = 152 + 128 + 13 * 6 + i
    perm[152 + 19 * 12 + 12 + 44 + 2 * i + 1] = 152 + 128 + 85 + 13 * 6 + i
m = m[perm][:,perm]
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

