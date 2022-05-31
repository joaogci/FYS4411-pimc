import numpy as np
import matplotlib.pyplot as plt
import matplotlib

plt.style.use('seaborn')
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

FOLDER = "results/"
SAVE_FOLDER = "figures/1D_L/"

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
    
    if i == 3:
        print("\(T/J\) & \(\langle E \ range\) & \(C\) & \(\langle m \ rangle\) & \(\langle m^2 \ rangle\) & \(\langle m \ rangle_s\) & \(\langle m^2 \ rangle_s\) & \(\chi\)")
        for j in range(0, T_vals, 5):
            print(f"\({T[i, j]:.2f}\) & \({E[i, j]:.4f} \pm {E_std[i, j]:.4f}\) & \({C[i, j]:.4f} \pm {C_std[i, j]:.4f}\) & \({m[i, j]:.4f} \pm {m_std[i, j]:.4f}\) & \({m2[i, j]:.4f} \pm {m2_std[i, j]:.4f}\) & \({ms[i, j]:.4f} \pm {ms_std[i, j]:.4f}\) & \({m2s[i, j]:.4f} \pm {m2s_std[i, j]:.4f}\) & \({m_sus[i, j]:.4f} \pm {m_sus_std[i, j]:.4f}\)")

plt.figure(1, figsize=(3, 2.25))
for i in range(L_vals):
    plt.plot(T[i, :], E[i, :], ".-", label=rf"$L=${L[i]}")
plt.xlabel(r"$T/J$", fontsize=10)
plt.ylabel(r"$\langle E \rangle$", fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.legend(fontsize=14)
plt.savefig(SAVE_FOLDER + "1D_heisenberg_E_vs_T.eps", bbox_inches="tight")

plt.figure(2, figsize=(3, 2.25))
for i in range(L_vals):
    plt.plot(T[i, :], C[i, :], ".-", label=rf"$L=${L[i]}")
plt.xlabel(r"$T/J$", fontsize=10)
plt.ylabel(r"$C$", fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.legend(fontsize=14)
plt.savefig(SAVE_FOLDER + "1D_heisenberg_C_vs_T.eps", bbox_inches="tight")

plt.figure(3, figsize=(3, 2.25))
for i in range(L_vals):
    plt.plot(T[i, :], m[i, :], ".-", label=rf"$L=${L[i]}")
plt.xlabel(r"$T/J$", fontsize=10)
plt.ylabel(r"$\langle m \rangle$", fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.legend(fontsize=14)
plt.savefig(SAVE_FOLDER + "1D_heisenberg_m_vs_T.eps", bbox_inches="tight")

plt.figure(4, figsize=(3, 2.25))
for i in range(L_vals):
    plt.plot(T[i, :], m2[i, :], ".-", label=rf"$L=${L[i]}")
plt.xlabel(r"$T/J$", fontsize=10)
plt.ylabel(r"$\langle m^2 \rangle$", fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.legend(fontsize=14)
plt.savefig(SAVE_FOLDER + "1D_heisenberg_m2_vs_T.eps", bbox_inches="tight")

plt.figure(5, figsize=(3, 2.25))
for i in range(L_vals):
    plt.plot(T[i, :], ms[i, :], ".-", label=rf"$L=${L[i]}")
plt.xlabel(r"$T/J$", fontsize=10)
plt.ylabel(r"$\langle m \rangle_s$", fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.legend(fontsize=14)
plt.savefig(SAVE_FOLDER + "1D_heisenberg_msvs_T.eps", bbox_inches="tight")

plt.figure(6, figsize=(3, 2.25))
for i in range(L_vals):
    plt.plot(T[i, :], m2s[i, :], ".-", label=rf"$L=${L[i]}")
plt.xlabel(r"$T/J$", fontsize=10)
plt.ylabel(r"$\langle m^2 \rangle_s$", fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.legend(fontsize=14)
plt.savefig(SAVE_FOLDER + "1D_heisenberg_m2s_vs_T.eps", bbox_inches="tight")

plt.figure(7, figsize=(3, 2.25))
for i in range(L_vals):
    plt.plot(T[i, :], m_sus[i, :], ".-", label=rf"$L=${L[i]}")
plt.xlabel(r"$T/J$", fontsize=10)
plt.ylabel(r"$\chi$", fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.legend(fontsize=14)
plt.savefig(SAVE_FOLDER + "1D_heisenberg_m_sus_vs_T.eps", bbox_inches="tight")

plt.figure(8, figsize=(3, 2.25))
for i in range(L_vals):
    plt.plot(T[i, :], binder[i, :], ".-", label=rf"$L=${L[i]}")
plt.xlabel(r"$T/J$", fontsize=10)
plt.ylabel(r"$U_L$", fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.legend(fontsize=14)
plt.savefig(SAVE_FOLDER + "1D_heisenberg_binder_vs_T.eps", bbox_inches="tight")

# plt.show()

