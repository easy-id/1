import matplotlib.pyplot as plt
import numpy as np

#g = 9.8
g = np.array([0,0,9.8])
v0 = 600
th = 45
k = [0, 0.02, 0.04, 0.06, 0.08, 0.1]
def calc(k):
    x0 = np.array([0,0,0], 'float64')
    v0x = np.array([v0 * np.cos(np.radians(th)), 0, v0 * np.sin(np.radians(th))])

    t = 0
    dt = 0.01
    x = np.array([0, 0, 0], 'float64')
    vx = v0x

    T = [t]
    X = [x[0]]
    Z = [x[2]]
    Vx = [vx[0]]
    Vz = [vx[2]]

    while x[2] >= 0:
        t += dt
        #ax = np.array([-k * vx[0], 0, -k * vx[2] - g])
        ax = -k * vx - g
        vx += ax * dt
        x += vx * dt
        X.append(x[0])
        Z.append(x[2])
        Vx.append(vx[0])
        Vz.append(vx[2])
        T.append(t)
    print("T = {:.2f} R = {:.3f}".format(t,x[0]))
    plt.plot(X,Z)

for kk in k:
    calc(kk)
plt.grid(True)
plt.legend(k)
plt.show()