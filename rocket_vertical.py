import matplotlib.pyplot as plt
meanThrust = 37 * 10**6
exhaustVel = 2600
rocketMass = 0.7e+6
fuelMass = 2.1e+6
v0 = 0
g = 9.8
alpha = meanThrust/exhaustVel
burnoutTime = fuelMass/alpha
dt = 0.1
t = 0
z = 0
v = v0

T = [t]
V = [v0]
Z = [z]
while fuelMass >0:
    fuelMass += -alpha*dt
    if fuelMass < 0:
        fuelMass = 0
    a = -g + meanThrust/(rocketMass+fuelMass)
    v += a * dt
    z += v * dt
    t += dt
    T.append(t)
    V.append(v)
    Z.append(z)
plt.plot(T,V)
plt.grid(True)
plt.figure()
plt.plot(T,Z)
plt.grid(True)
plt.show()