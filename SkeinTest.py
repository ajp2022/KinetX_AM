import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Parameters
step = 0.1  # resolution, time step period for each xyz calculation
k = 4
dp = 0.08  # change to modify ER, minimum distance between fibers, center to center
h = 0.3  # height of each layer
c1 = 2  # standard deviation coefficient

H = 10  # total height of the skin

p = dp / (np.pi)
period = (H - h) / p
n = (k - 1) / k

t = np.arange(0, period + step, step)

t1 = period * np.array([0, 1/5, 2/5, 3/5, 4/5, 1])
r1 = H * np.array([0.25, 0.4, 0.55, 0.4, 0.36, 0.25])

pol = CubicSpline(t1, r1)

a = pol(t)
c = a / c1

theta = t
rho = a * np.cos(n * t)

z = h * (np.exp(-(rho ** 2 / (2 * c ** 2))))
z = z - z[0]
dz = p * theta
z = z + dz
x, y = rho * np.cos(theta), rho * np.sin(theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot3D(x, y, z, color='gray', linewidth=1)
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([0, 10])
ax.view_init(elev=0, azim=-90)
ax.axis('off')

plt.show()


s = np.sum(np.sqrt(np.diff(x)**2 + np.diff(y)**2 + np.diff(z)**2))
er = s / H

np.savez('4nozzle.npz', x=x, y=y, z=z)

print(f"Effective radius (ER): {er}")


# Assuming you've previously converted and saved your MATLAB data ('x', 'y', 'z' arrays) to a '.npz' file
data = np.load('4nozzle.npz')
x = data['x']
y = data['y']
z = data['z']

# Parameters
speed = 5 * 60  # mm/min

# Prepare the motion matrix
motion = np.column_stack((x, y, z))
motion[:, 1]  # Adjust Y coordinates

# Generate G-code
code = ""
for i in range(len(motion)):
    x_str = f"X{motion[i, 0]:2.13f}"
    y_str = f"Y{motion[i, 1]:2.13f}"
    z_str = f"Z{motion[i, 2]:2.13f}"
    f_str = f"F{speed:2.13f}"
    code += f"G1 {x_str} {y_str} {z_str} {f_str}\n"

# Save to a text file
#with open('generated_gcode.txt', 'w') as file:
#    file.write(code)

print(code)
