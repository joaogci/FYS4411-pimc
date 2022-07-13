import numpy as np

beta = 1.0 / 1.05
delta = 1.0
h = 0.0
np.random.seed(seed=4)

N = 8
Nb = N  # PBC

M = np.max([4, N // 4])
n = 0

# SSE State
spin = np.ones(N, dtype=np.int64)
op_string = np.zeros(M, dtype=np.int64)

spin = np.array([1, 1, -1, -1, 1, -1, 1, -1])
print(f"Spin State = {spin}")
op_string = np.array([4, 0, 9, 13, 6, 0, 0, 4, 13, 0, 9, 14], dtype=np.int64)
M = 12
n = 8
print(f"n = {n}")
print("p | a[p]  |  b[p]  |  opstring[p] ")
for p in range(M):
    a = 0
    b = 0
    if op_string[p] != 0:
        a = np.mod(op_string[p], 2) + 1
        b = op_string[p] // 2 - 1
    print(f"{p} |   {a}   |   {b}    |    {op_string[p]}")

# Lattice Geometry
site = np.zeros((Nb, 2), dtype=np.int64)
for b in range(N):
    site[b, 0] = b
    site[b, 1] = np.mod(b + 1, N) 

def diag_update():
    global n, spin, op_string
    
    for p in range(M):
        if op_string[p] == 0:
            b = np.random.randint(0, Nb)

            prob = 0.0
            if spin[site[b, 0]] != spin[site[b, 1]]:
                prob = delta * 0.5
            elif spin[site[b, 0]] == spin[site[b, 1]] and spin[site[b, 1]] == 1:
                prob = h

            if np.random.rand() <= np.min([1, Nb * beta * prob / (M - n)]):
                op_string[p] = 2 * (b + 1)
                n += 1

        elif np.mod(op_string[p], 2) == 0:
            b = op_string[p] // 2 - 1
            
            prob = np.inf
            if spin[site[b, 0]] != spin[site[b, 1]]:
                prob = delta * 0.5
            elif spin[site[b, 0]] == spin[site[b, 1]] and spin[site[b, 1]] == 1:
                prob = h
            
            if np.random.rand() <= np.min([1, (np.array([M - n + 1]) / (beta * Nb * prob))[0]]):
                op_string[p] = 0
                n += -1
        
        else:
            b = op_string[p] // 2 - 1
            spin[site[b, 0]] = - spin[site[b, 0]]
            spin[site[b, 1]] = - spin[site[b, 1]]

def create_vertex_list():
    vtx = np.zeros(M, dtype=np.int64)
    link = np.zeros(4 * M, dtype=np.int64) - 1
    
    first = np.zeros(N, dtype=np.int64) - 1
    last = np.zeros(N, dtype=np.int64) - 1
    
    for p in range(M):
        if op_string[p] == 0:
            continue
        elif np.mod(op_string[p], 2) != 0:
            # vtx type: 
            b = op_string[p] // 2 - 1
            spin[site[b, 0]] = - spin[site[b, 0]]
            spin[site[b, 1]] = - spin[site[b, 1]]
            
            # record legs
            l1 = - spin[site[b, 0]]
            l2 = - spin[site[b, 1]]
            l3 = spin[site[b, 0]]
            l4 = spin[site[b, 1]]
            
            if l1 == l2 and l2 == l3 and l3 == l4 and l4 == -1:
                vtx[p] = 1
            elif l1 == -1 and l2 == 1 and l3 == -1 and l4 == 1:
                vtx[p] = 2
            elif l1 == 1 and l2 == -1 and l3 == 1 and l4 == -1:
                vtx[p] = 3
            elif l1 == -1 and l2 == 1 and l3 == 1 and l4 == -1:
                vtx[p] = 4
            elif l1 == 1 and l2 == -1 and l3 == -1 and l4 == 1:
                vtx[p] = 5
            elif l1 == l2 and l2 == l3 and l3 == l4 and l4 == 1:
                vtx[p] = 6
            # print(f"off-diag with {l1=}; {l2=}; {l3=}; {l4=}; type: {vtx[p]}")
        elif np.mod(op_string[p], 2) == 0:
            b = op_string[p] // 2 - 1
            
            l1 = spin[site[b, 0]]
            l2 = spin[site[b, 1]]
            l3 = spin[site[b, 0]]
            l4 = spin[site[b, 1]]
           
            if l1 == -1 and l2 == -1 and l3 == -1 and l4 == -1:
                vtx[p] = 1
            elif l1 == -1 and l2 == 1 and l3 == -1 and l4 == 1:
                vtx[p] = 2
            elif l1 == 1 and l2 == -1 and l3 == 1 and l4 == -1:
                vtx[p] = 3
            elif l1 == -1 and l2 == 1 and l3 == 1 and l4 == -1:
                vtx[p] = 4
            elif l1 == 1 and l2 == -1 and l3 == -1 and l4 == 1:
                vtx[p] = 5
            elif l1 == 1 and l2 == 1 and l3 == 1 and l4 == 1:
                vtx[p] = 6
            # print(f"diag with {l1=}; {l2=}; {l3=}; {l4=}; type: {vtx[p]}")
            
        v0 = 4 * p
        bond = op_string[p] // 2 - 1
        
        i1 = site[bond, 0]
        i2 = site[bond, 1]
        
        v1 = last[i1]
        v2 = last[i2]
        
        if v1 != -1:
            link[v1] = v0
            link[v0] = v1
        else:
            first[i1] = v0
        
        if v2 != -1:
            link[v2] = v0 + 1
            link[v0 + 1] = v2
        else:
            first[i2] = v0 + 1
            
        last[i1] = v0 + 2
        last[i2] = v0 + 3
    
    for i in range(N):
        f = first[i]
        if f != -1:
            l = last[i]
            link[f] = l
            link[l] = f

    return link, vtx, first

link, vtx, first = create_vertex_list()
print(f"Vertex list = ")
for p in range(M):
    print(f"[{4 * p}] {link[4 * p]},  " + 
          f"[{4 * p + 1}] {link[4 * p + 1]},  " +
          f"[{4 * p + 2}] {link[4 * p + 2]},  " +
          f"[{4 * p + 3}] {link[4 * p + 3]}; " + 
          f"type: {vtx[p]}")
    
# diag_update()
# print()
# print("After diag_update()")
# print(f"Spin State = {spin}")
# print(f"n = {n}")
# print("p | a[p]  |  b[p]  |  opstring[p] ")
# for p in range(M):
#     a = 0
#     b = 0
#     if op_string[p] != 0:
#         a = np.mod(op_string[p], 2) + 1
#         b = op_string[p] // 2 - 1
#     print(f"{p} |   {a}   |   {b}    |    {op_string[p]}")

# link, vtx, first = create_vertex_list()
# print(f"Vertex list = ")
# for p in range(M):
#     print(f"[{4 * p}] {link[4 * p]},  " + 
#           f"[{4 * p + 1}] {link[4 * p + 1]},  " +
#           f"[{4 * p + 2}] {link[4 * p + 2]},  " +
#           f"[{4 * p + 3}] {link[4 * p + 3]}; " + 
#           f"type: {vtx[p]}")

def prob_exit(li, le, vtx):
    spin_leg = np.array([leg_spin(i, vtx) for i in range(4)])
    

def new_vtx(li, le, vtx):
    if li == le:
        return vtx
    
    if vtx == 1:
        if li == 1:
            if le == 3:
                return 3
            if le == 4:
                return 5
        if li == 2:
            if le == 4:
                return 2
            if le == 3:
                return 4
        if li == 3:
            if le == 1:
                return 3
            if le == 2:
                return 4
        if li == 4:
            if le == 2:
                return 2
            if le == 1:
                return 5
    elif vtx == 2:
        if li == 1:
            if le == 3:
                return 6
            if le == 2:
                return 5
        if li == 2:
            if le == 4:
                return 1
            if le == 1:
                return 5
        if li == 3:
            if le == 1:
                return 6
            if le == 4:
                return 4
        if li == 4:
            if le == 2:
                return 1
            if le == 3:
                return 4
    elif vtx == 3:
        if li == 1:
            if le == 3:
                return 1
            if le == 2:
                return 4
        if li == 2:
            if le == 4:
                return 6
            if le == 1:
                return 4
        if li == 3:
            if le == 1:
                return 4
            if le == 4:
                return 5
        if li == 4:
            if le == 2:
                return 6
            if le == 3:
                return 5
    elif vtx == 4:
        if li == 1:
            if le == 4:
                return 6
            if le == 2:
                return 3
        if li == 2:
            if le == 3:
                return 1
            if le == 1:
                return 3
        if li == 3:
            if le == 2:
                return 1
            if le == 4:
                return 2
        if li == 4:
            if le == 1:
                return 6
            if le == 3:
                return 2
    elif vtx == 5:
        if li == 1:
            if le == 4:
                return 1
            if le == 2:
                return 2
        if li == 2:
            if le == 3:
                return 6
            if le == 1:
                return 2
        if li == 3:
            if le == 2:
                return 6
            if le == 4:
                return 3
        if li == 4:
            if le == 1:
                return 1
            if le == 3:
                return 3
    elif vtx == 6:
        if li == 1:
            if le == 3:
                return 2
            if le == 4:
                return 4
        if li == 2:
            if le == 4:
                return 3
            if le == 3:
                return 5
        if li == 3:
            if le == 1:
                return 2
            if le == 2:
                return 5
        if li == 4:
            if le == 2:
                return 3
            if le == 1:
                return 4

def leg_spin(l, vtx):
    if vtx == 1:
        return -1
    elif vtx == 2:
        if l % 2 == 0:
            return 1
        return -1
    elif vtx == 3:
        if l % 2 == 0:
            return -1
        return 1
    elif vtx == 4:
        if l == 1 or l == 4:
            return -1
        return 1
    elif vtx == 5:
        if l == 1 or l == 4:
            return 1
        return -1
    elif vtx == 6:
        return 1

op_type = np.array([0, 0, 0, 1, 1, 0])
def loop_update():
    global spin, op_string
    
    link, vtx_type, first = create_vertex_list()
    new_vtx_type = vtx_type
    
    j0 = np.random.randint(0, 4 * n)
    while link[j0] < 0:
        j0 = np.random.randint(0, 4 * n)
    
    j_in = j0
    while True:
        link[j_in] = -2
        p = j_in // 4 
        l_i = np.mod(j_in, 4)
        for l_e in range(4):
            if np.random.rand() <= prob_exit(l_i, l_e, vtx_type[p]):
                new_vtx_type[p] = new_vtx(l_i, l_e, vtx_type[p])
                break
        j_out = 4 * p + l_e
        j_in = link[j_out]
        link[j_out] = -2
        
        if j_in == j0:
            break
    
    for p in range(M):
        b = op_string[p] // 2 - 1
        op_string[p] = 2 * b + op_type[new_vtx_type[p]]
        
    for i in range(N):
        if first[i] != -1:
            p = first[i] // 4
            l = np.mod(first[i], 4)
            spin[i] = leg_spin(l, new_vtx_type[p])
        else:
            if np.random.rand() <= 0.5:
                spin[i] = - spin[i]
    
        
        
        
        
        
    
    
    
    
        
 

