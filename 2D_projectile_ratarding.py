# Simple trajectory calculation

import matplotlib.pyplot as plt
import numpy as np

x0 = 0
z0 = 0
g = 9.8
v0 = 600
th = 45
k = 0.1
v0x = v0 * np.cos(np.radians(th))
v0z = v0 * np.sin(np.radians(th))
t = 0
dt = 0.01
x = 0
z = 0
vx = v0x
vz = v0z
T = [t]
X = [x]
Z = [z]
Vx = [vx]
Vz = [vz]

while z >= 0:
    t += dt
    az = -k * vz - g
    ax = -k * vx
    vx += ax * dt
    vz += az * dt
    x += vx * dt
    z += vz * dt
    X.append(x)
    Z.append(z)
    Vx.append(vx)
    Vz.append(vz)
    T.append(t)
print("T = {:.2f} R = {:.3f}".format(t,x))
plt.plot(X,Z)
plt.grid(True)
plt.show()