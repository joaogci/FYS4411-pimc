import numpy as np
import matplotlib.pyplot as plt
import matplotlib

plt.style.use('seaborn')
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

FOLDER = "results/"
SAVE_FOLDER = "figures/"

filenames = ["1D_heisenberg_L16_h0_delta1.csv", "1D_heisenberg_L32_h0_delta1.csv", "1D_heisenberg_L64_h0_delta1.csv", "1D_heisenberg_L128_h0_delta1.csv"]

T_vals = 50
L_vals = len(filenames)
L = np.array([16, 32, 64, 128])

T = np.zeros((L_vals, T_vals))
E = np.zeros((L_vals, T_vals))
E_std = np.zeros((L_vals, T_vals))
C = np.zeros((L_vals, T_vals))
C_std = np.zeros((L_vals, T_vals))

m = np.zeros((L_vals, T_vals))
m_std = np.zeros((L_vals, T_vals))
m2 = np.zeros((L_vals, T_vals))
m2_std = np.zeros((L_vals, T_vals))
m4 = np.zeros((L_vals, T_vals))
m4_std = np.zeros((L_vals, T_vals))

ms = np.zeros((L_vals, T_vals))
ms_std = np.zeros((L_vals, T_vals))
m2s = np.zeros((L_vals, T_vals))
m2s_std = np.zeros((L_vals, T_vals))
m4s = np.zeros((L_vals, T_vals))
m4s_std = np.zeros((L_vals, T_vals))

n = np.zeros((L_vals, T_vals))
n_std = np.zeros((L_vals, T_vals))
n2 = np.zeros((L_vals, T_vals))

m_sus = np.zeros((L_vals, T_vals))
m_sus_std = np.zeros((L_vals, T_vals))

binder = np.zeros((L_vals, T_vals))
binder_std = np.zeros((L_vals, T_vals))
binders = np.zeros((L_vals, T_vals))
binders_std = np.zeros((L_vals, T_vals))
# beta,n,n2,n_std,E,E_std,C,C_std,m,m_std,m2,m2_std,ms,ms_std,m2s,m2s_std,sus,sus_std

for i, filename in enumerate(filenames):
    with open(FOLDER + filename, "r") as file:
        header = file.readline()
        
        for j in range(T_vals):
            T[i, j], n[i, j], n2[i, j], n_std[i, j], E[i, j], E_std[i, j], C[i, j], C_std[i, j], m[i, j], m_std[i, j], m2[i, j], m2_std[i, j], m4[i, j], m4_std[i, j], ms[i, j], ms_std[i, j], m2s[i, j], m2s_std[i, j], m4s[i, j], m4s_std[i, j], m_sus[i, j], m_sus_std[i, j], binder[i, j], binder_std[i, j], binders[i, j], binders_std[i, j] = [float(x) for x in file.readline().strip().split(",")]
        T[i, :] = 1.0 / T[i, :]

plt.figure(1)
for i in range(L_vals):
    plt.plot(T[i, :], E[i, :], ".-", label=rf"$L=${L[i]}")
plt.xlabel(r"$T/J$", fontsize=16)
plt.ylabel(r"$\langle E \rangle$", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=16)

plt.figure(2)
for i in range(L_vals):
    plt.plot(T[i, :], C[i, :], ".-", label=rf"$L=${L[i]}")
plt.xlabel(r"$T/J$", fontsize=16)
plt.ylabel(r"$C$", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=16)

plt.figure(3)
for i in range(L_vals):
    plt.plot(T[i, :], m[i, :], ".-", label=rf"$L=${L[i]}")
plt.xlabel(r"$T/J$", fontsize=16)
plt.ylabel(r"$\langle m \rangle$", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=16)

plt.figure(4)
for i in range(L_vals):
    plt.plot(T[i, :], m2[i, :], ".-", label=rf"$L=${L[i]}")
plt.xlabel(r"$T/J$", fontsize=16)
plt.ylabel(r"$\langle m^2 \rangle$", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=16)

plt.figure(5)
for i in range(L_vals):
    plt.plot(T[i, :], ms[i, :], ".-", label=rf"$L=${L[i]}")
plt.xlabel(r"$T/J$", fontsize=16)
plt.ylabel(r"$\langle m \rangle_s$", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=16)

plt.figure(6)
for i in range(L_vals):
    plt.plot(T[i, :], m2s[i, :], ".-", label=rf"$L=${L[i]}")
plt.xlabel(r"$T/J$", fontsize=16)
plt.ylabel(r"$\langle m^2 \rangle_s$", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=16)

plt.figure(7)
for i in range(L_vals):
    plt.plot(T[i, :], m_sus[i, :], ".-", label=rf"$L=${L[i]}")
plt.xlabel(r"$T/J$", fontsize=16)
plt.ylabel(r"$\langle \chi \rangle$", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=16)

plt.figure(8)
for i in range(L_vals):
    plt.plot(T[i, :], binder[i, :], ".-", label=rf"$L=${L[i]}")
plt.xlabel(r"$T/J$", fontsize=16)
plt.ylabel(r"$\langle \chi \rangle$", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=16)

plt.show()

