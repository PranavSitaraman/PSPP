
import math
# T R S A B C N
compare = [
    [0,     60,     60,     109.5,    109.5,    109.5,    180],
    [60,    0,      120,    99.6,    150.9,    57.3,     120],
    [60,    120,    0,      99.6,    57.3,     150.9,    120],
    [109,   99.6,   99.6,    0,      109.5,    109.5,    70.5],
    [109,   150.9,  57.3,     109.5,    0,      109.5,    70.5],
    [109,   57.3,   150.9,    109.5,    109.5,      0,    70.5],
    [180,   120,    120,    70.5,     70.5,     70.5,     0]
]
triangle = [1, 2, 6]
print("BB84-Parity")
prob = 0
for i in range(7):
    for j in range(7):
        if i in triangle:
            factorone = 1/6
        else:
            factorone = 1/8
        if j in triangle:
            factortwo = 1/6
        else:
            factortwo = 1/8
        prob += factorone * factortwo * pow(math.cos(compare[i][j]/2 * math.pi/180), 4)
print("Proportion of Key Eavesdropped: ", prob)
prob = 0
for i in range(7):
    factorone = 1/7
    prob += factorone * (pow(math.cos(compare[i][i]/2 * math.pi/180), 4) + pow(1 - pow(math.cos(compare[i][i]/2 * math.pi/180), 2), 2))
print("Proportion of Checked Bits Match (No Interference): ", prob)
prob = 0
for i in range(7):
    for j in range(7):
        if i in triangle:
            factorone = 1/6
        else:
            factorone = 1/8
        if j in triangle:
            factortwo = 1/6
        else:
            factortwo = 1/8
        prob += factorone * factortwo * (pow(math.cos(compare[i][j]/2 * math.pi/180), 4) + pow(1 - pow(math.cos(compare[i][j]/2 * math.pi/180), 2), 2))
print("Proportion of Checked Bits Match (Interference): ", prob)
print("Proportion of Key Incorrect: ", 1 - prob)