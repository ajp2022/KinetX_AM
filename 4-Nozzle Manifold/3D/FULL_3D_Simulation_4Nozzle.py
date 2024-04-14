import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
from mpl_toolkits.mplot3d import Axes3D

box_x = [0, 50, 50, 0, 0]
box_y = [0, 0, 60, 60, 0]
box_z = [0, 0, 60, 60, 0]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-5, 60])
ax.set_ylim([-5, 60])
ax.set_zlim([0, 40])
#'''
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
#'''

SKEIN_HEIGHT = 8
offset = 10.617
operations = 0
total_length = 0
s_total = 0
s_length = 1111.3157004470734

def skein(x_coord, y_coord, z_coord, color):
    step = 0.05
    k = 4  # Number of loops in each layer
    dp = 0.062  # Distance between threads in mm
    h = 0.2  # Height of one layer
    c1 = 4  # Standard deviation in z
    H = 8  # Total height

    p = dp / np.pi
    period = (H - h) / p
    n = (k - 1) / k
    t = np.arange(0, period + step, step)
    t1 = period * np.array([0, 1/5, 2/5, 3/5, 4/5, 1])
    r1 = H * np.array([0.15, 0.2, 0.35, 0.35, 0.2, 0.15]) #ER: 92 BCC
    #r1 = H * np.array([0.25, 0.4, 0.55, 0.4, 0.36, 0.25]) #ER: 132 Non-BCC
    pol = np.polyfit(t1, r1, 3)
    a = np.polyval(pol, t)
    c = a / c1
    theta = t
    rho = a * np.cos(n * t)
    z = h * (np.exp(-((rho ** 2) / (2 * c ** 2))))
    z = z - z[0]
    dz = p * theta
    z = z + dz
    x, y = rho * np.cos(theta), rho * np.sin(theta)
    ax.plot3D(x + x_coord, y + y_coord, z + z_coord, color=color, linewidth=0.5, alpha = 0.35)

HeightLayers = 7
HorizontalIterations = 1
VerticalIterations = 1

Test_Height_Offset = 0

color_index = 0
colors = ['purple', 'blue', 'green', 'orange', 'red', 'yellow']
for z in range(HeightLayers):
    for h in range(HorizontalIterations):
        if z % 2 == 0:
            for v in range(VerticalIterations):
                #'''
                skein(2*h*offset, offset+offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                operations += 1
                s_total += s_length
                skein(2*h*offset, offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                operations += 1
                s_total += s_length
                skein((1+2*h)*offset, offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                operations += 1
                s_total += s_length
                skein((1+2*h)*offset, offset+offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                operations += 1
                s_total += s_length
                color_index += 3
                #'''
            for v in range(VerticalIterations):
                #'''
                skein((0.5+2*h)*offset, offset/2+offset+offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                operations += 1
                s_total += s_length
                skein((0.5+2*h)*offset, offset/2+offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                operations += 1
                s_total += s_length
                skein((1.5+2*h)*offset, offset/2+offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                operations += 1
                s_total += s_length
                skein((1.5+2*h)*offset, offset/2+offset+offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                operations += 1
                s_total += s_length
                color_index += 4
                #'''
        else:
            for v in range(VerticalIterations):
                #'''
                skein(2*h*offset + offset/2, offset+offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                operations += 1
                s_total += s_length
                skein(2*h*offset + offset/2, offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                operations += 1
                s_total += s_length
                skein((1+2*h)*offset + offset/2, offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                operations += 1
                s_total += s_length
                skein((1+2*h)*offset + offset/2, offset+offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                operations += 1
                s_total += s_length
                color_index += 5
                #'''
            for v in range(VerticalIterations):
                #'''
                skein((0.5+2*h)*offset + offset/2, offset/2+offset+offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                operations += 1
                s_total += s_length
                skein((0.5+2*h)*offset + offset/2, offset/2+offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                operations += 1
                s_total += s_length
                skein((1.5+2*h)*offset + offset/2, offset/2+offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                operations += 1
                s_total += s_length
                skein((1.5+2*h)*offset + offset/2, offset/2+offset+offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                operations += 1
                s_total += s_length
                color_index += 6
                #'''
    Test_Height_Offset += SKEIN_HEIGHT/2 + 0.5
print(s_total)
print(operations)
plt.show()