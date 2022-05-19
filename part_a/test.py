import numpy as np

N = 20
a = 0.5
eps = 1.4
x = np.zeros(N)
N_cf = 10000
N_corr = 20
corr = np.zeros(N)
G = np.zeros((N_cf, N))

def S(j, x):
    j_next = (j+1)%N
    j_prev = (j-1)%N

    return a*x[j]**2/2 + x[j]*(x[j] - x[j_next] - x[j_prev])/a

def update(x):
    for j in range(N):
        old_x = x[j]
        old_Sj = S(j, x)
        x[j] += np.random.uniform(-eps, eps)
        dS = S(j, x) - old_Sj

        if np.exp(-dS) < np.random.rand():
            x[j] = old_x

def compute_G(x, n):
    g = 0
    for j in range(N):
        g += x[j] * x[(j+n)%N]

    return g/N

def MCaverage(x, G):
    for j in range(10 * N_corr):     # Thermalize
        update(x)

    for alpha in range(N_cf):
        for j in range(N_corr):
            update(x)

        for n in range(N):
            G[alpha][n] = compute_G(x, n)

    for n in range(N):
        avg_G = 0
        for alpha in range(N_cf):
            avg_G += G[alpha][n]
        avg_G = avg_G/N_cf
        corr[n] = avg_G

MCaverage(x, G)

'''
def del_E(x):
    def _G(x, n):
        tmp = 0
        for j in range(N):
            tmp += x[(j+n)%N] * x[j]
        return tmp/N

    gn = _G(x)<++>
'''

print(f"First average energy = {np.log(corr[0]/corr[1])/a}")
