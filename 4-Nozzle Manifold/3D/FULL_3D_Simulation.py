import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
from mpl_toolkits.mplot3d import Axes3D

box_x = [0, 50, 50, 0, 0]
box_y = [0, 0, 60, 60, 0]
box_z = [0, 0, 60, 60, 0]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-10, 60])
ax.set_ylim([-10, 60])
ax.set_zlim([-10, 60])

SKEIN_HEIGHT = 7
offset = 10.617
operations = 0
total_length = 0

def skein(x_coord, y_coord, z_coord, color):
    # Parameters for the path calculation
    step = 0.1  # resolution, time step period for each xyz calculation
    k = 4
    dp = 0.08  # change to modify ER, minimum distance between fibers, center to center
    h = 0.3  # height of each layer
    c1 = 2  # standard deviation coefficient
    H = SKEIN_HEIGHT  # total height of the skein

    p = dp / (np.pi)
    period = (H - h) / p
    n = (k - 1) / k
    t = np.arange(0, period + step, step)
    t1 = period * np.array([0, 1/5, 2/5, 3/5, 4/5, 1])
    r1 = H * np.array([0.25, 0.4, 0.55, 0.4, 0.36, 0.25])
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
    ax.plot3D(x + x_coord, y + y_coord, z + z_coord, color=color, linewidth=1, alpha = 0.5)

HeightLayers = 2
HorizontalIterations = 2
VerticalIterations = 2

Test_Height_Offset = 0

colors = ['red', 'blue', 'green', 'orange', 'purple', 'yellow']
for z in range(HeightLayers):
    color_index = 0
    for h in range(HorizontalIterations):
        if z % 2 == 0:
            for v in range(VerticalIterations):
                skein(2*h*offset, offset+offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                skein(2*h*offset, offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                skein((1+2*h)*offset, offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                skein((1+2*h)*offset, offset+offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                color_index += 1
            for v in range(VerticalIterations):
                skein((0.5+2*h)*offset, offset/2+offset+offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                skein((0.5+2*h)*offset, offset/2+offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                skein((1.5+2*h)*offset, offset/2+offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                skein((1.5+2*h)*offset, offset/2+offset+offset*2*v, Test_Height_Offset, colors[color_index % len(colors)])
                color_index += 1
        else:
            for v in range(VerticalIterations):
                skein(2*h*offset + offset/4, offset+offset*2*v + offset/4, Test_Height_Offset, colors[color_index % len(colors)])
                skein(2*h*offset + offset/4, offset*2*v + offset/4, Test_Height_Offset, colors[color_index % len(colors)])
                skein((1+2*h)*offset + offset/4, offset*2*v + offset/4, Test_Height_Offset, colors[color_index % len(colors)])
                skein((1+2*h)*offset + offset/4, offset+offset*2*v + offset/4, Test_Height_Offset, colors[color_index % len(colors)])
                color_index += 1
            for v in range(VerticalIterations):
                skein((0.5+2*h)*offset + offset/4, offset/2+offset+offset*2*v + offset/4, Test_Height_Offset, colors[color_index % len(colors)])
                skein((0.5+2*h)*offset + offset/4, offset/2+offset*2*v + offset/4, Test_Height_Offset, colors[color_index % len(colors)])
                skein((1.5+2*h)*offset + offset/4, offset/2+offset*2*v + offset/4, Test_Height_Offset, colors[color_index % len(colors)])
                skein((1.5+2*h)*offset + offset/4, offset/2+offset+offset*2*v + offset/4, Test_Height_Offset, colors[color_index % len(colors)])
                color_index += 1
    Test_Height_Offset += SKEIN_HEIGHT/2

plt.show()