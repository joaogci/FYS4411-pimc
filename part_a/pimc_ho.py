import numpy as np
import matplotlib.pyplot as plt

def action(x, a):
    S = 0.0
    for j in range(x.shape[0] - 1):
        S += (x[j + 1] - x[j])**2 / (2 * a) + 0.5 * a * x[j] * x[j]
    return S

'''
def S(i, x):
    jp = (j+1) % x.shape[0]
    jm = (j-1) % x.shape[0]


def update(x):
    for i in range(x.shape[0]):
        old_x = x[i]
        old_S = action(x)<++>
'''

a = 0.5
N = 20
t_0 = 0.0
t_f = a * N

equi_cycles = int(1e4)
mc_cycles = int(1e4)
n_corr = 20
n_bins = 10
step_size = 0.25     # 0.025 originally originally

# Init positions array
x = np.zeros(N)
x_new = np.zeros(N)

G_bins = np.zeros((n_bins, N))
energy_bins = np.zeros(n_bins)

# MC update
for t in range(equi_cycles):
    x_new = x + np.random.uniform(-step_size, step_size, x.shape[0])
    
    dif = action(x_new, a) - action(x, a)
    #if dif <= 0 or np.random.rand() <= np.exp(- dif):
    if np.exp(-dif) >= np.random.rand():    # If dif < 0 exp(-dif) > 1 >= rand() is always true
        x = x_new

for n in range(n_bins):
    G = np.zeros(N)
    energy = 0.0
    acc = 0

    for t in range(mc_cycles):
        for k in range(n_corr):
            x_new = x + np.random.uniform(-step_size, step_size, x.shape[0])
    
            dif = action(x_new, a) - action(x, a)
            if dif <= 0 or np.random.rand() <= np.exp(- dif):
                acc += 1
                x = x_new

        for dj in range(N):
            for j in range(N):
                G[dj] += x[(j + dj) % N] * x[j]
        G /= N
        energy += np.average(x * x)

    G_bins[n, :] = G / mc_cycles
    energy_bins[n] = energy / mc_cycles
    
    print(acc / (mc_cycles * n_corr))

G_mean = np.mean(G_bins, axis=0)
G_std = np.std(G_bins, axis=0)

energy_mean = np.mean(energy_bins)
energy_std = np.std(energy_bins)

first_excit_erg = np.log(G[0] / G[-1]) / (t_f - t_0)
print(f"{first_excit_erg=}")
print(f"{energy_mean=}; {energy_std=}")

plt.figure(1)
plt.errorbar(np.arange(t_0, t_f, a), G_mean, G_std)
plt.xlabel(r"$t$")
plt.ylabel(r"$G_{MC}(t)$")

plt.show()

