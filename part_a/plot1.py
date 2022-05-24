import numpy as np
import matplotlib.pyplot as plt

N = 20
'''
dE = np.zeros(N)
with open("delta_E.txt", "r") as infile:
    for i in range(N):
        dE[i] = float(infile.readline())
'''

data = np.loadtxt("delta_E_6.txt", dtype = float, delimiter = ", ")
#print(data)

mean = np.mean(data, axis=0)
std = np.std(data, axis=0)

ax = np.arange(0, N)

plt.scatter(ax, mean)
plt.scatter(ax, mean + std, alpha = 0.35, ls = "--", c = "k")
plt.scatter(ax, mean -std, alpha = 0.35, ls = "--", c = "k")

plt.show()
