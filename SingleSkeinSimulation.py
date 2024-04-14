import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Initial Parameters
step = 0.05 # resolution, time step period for each xyz calculation. smaller for smaller skeins
k = 4
dp = 0.062 # change to modify ER, minimum distance between fibers, center to center.
h = 0.2 # height of each layer
c1 = 4 # standard deviation coefficient
H = 8 # total height of skein

p = dp / (np.pi)
period = (H - h) / p
n = (k - 1) / k

t = np.arange(0, period + step, step)

t1 = period * np.array([0, 1/5, 2/5, 3/5, 4/5, 1])
#r1 = H * np.array([0.25, 0.4, 0.5, 0.4, 0.36, 0.25])
r1 = H * np.array([0.15, 0.2, 0.35, 0.35, 0.2, 0.15]) #ER: 92 BCC
pol = np.polyfit(t1, r1, 3)

a = np.polyval(pol, t)
c = a / c1

theta = t
rho = a * np.cos(n * t)

z = h * (np.exp(- (rho**2 / (2 * c**2))))
z = z - z[0]
dz = p * theta
z = z + dz
x, y = rho * np.cos(theta), rho * np.sin(theta)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot3D(x, y, z, color='gray', linewidth=1)
ax.view_init(elev=0, azim=-90)
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([0, 10])
ax.axis('off')

plt.show()

# Calculating the effective radius (er)
s = np.sum(np.sqrt(np.diff(x)**2 + np.diff(y)**2 + np.diff(z)**2))
er = s / H
print(s)

# Save the data
#np.savez('4nozzle.npz', x=x, y=y, z=z)
