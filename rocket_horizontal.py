import matplotlib.pyplot as plt
meanThrust = 37 * 10**6
exhaustVel = 2600
rocketMass = 0.7e+6
fuelMass = 2.1e+6
v0 = 1 * 10**3
alpha = meanThrust/exhaustVel
burnoutTime = fuelMass/alpha
dt = 0.1
t = 0
x = 0
v = v0

T = [t]
V = [v0]
X = [x]
while fuelMass >0:
    fuelMass += -alpha*dt
    a = meanThrust/(rocketMass+fuelMass)
    v += a * dt
    x += v * dt
    t += dt
    T.append(t)
    V.append(v)
    X.append(x)
plt.plot(T,V)
plt.grid(True)
plt.show()