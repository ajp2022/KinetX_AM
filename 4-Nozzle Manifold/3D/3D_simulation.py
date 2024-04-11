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

offset = 10.617
operations = 0
total_length = 0


def plot_dots_in_box(dot_coordinates):
    for x, y, z in dot_coordinates:
        plt.plot(x, y, z, 'bo', markersize = 3)
def plot_dots_in_box_interweaved(dot_coordinates):
    for x, y, z in dot_coordinates:
        plt.plot(x, y, z, 'ro', markersize = 3)

def skein(x_coord, y_coord, z_coord):
    # Parameters for the path calculation
    step = 0.1  # resolution, time step period for each xyz calculation
    k = 4
    dp = 0.08  # change to modify ER, minimum distance between fibers, center to center
    h = 0.3  # height of each layer
    c1 = 2  # standard deviation coefficient
    H = 10  # total height of the skein


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

    #s = np.sum(np.sqrt(np.diff(x)**2 + np.diff(y)**2 + np.diff(z)**2))
    #er = s / H
    #print(f"Effective radius (ER): {er}")

    speed = 5 * 60  # mm/min

    motion = np.column_stack((x, y, z))
    motion[:, 0] += x_coord
    motion[:, 1] += y_coord
    motion[:, 2] += z_coord

    skeingcode = ""
    for i in range(len(motion)):
        x_str = f"X{motion[i, 0]:2.13f}"
        y_str = f"Y{motion[i, 1]:2.13f}"
        z_str = f"Z{motion[i, 2]:2.13f}"
        f_str = f"F{speed:2.13f}"
        skeingcode += f"G1  {x_str}  {y_str}  {z_str}  {f_str}\n"
    print(skeingcode)

HeightLayers = 10
HorizontalIterations = 2
VerticalIterations = 2

#2D Simulation Code
for z in range(HeightLayers):
    for h in range(HorizontalIterations):
        if z % 2 == 0:
            for v in range(VerticalIterations):
                dot_coordinates = [(2*h*offset, offset+offset*2*v, offset*z/4), (2*h*offset, offset*2*v, offset*z/4), ((1+2*h)*offset, offset*2*v, offset*z/4), ((1+2*h)*offset, offset+offset*2*v, offset*z/4)]
                plot_dots_in_box(dot_coordinates)
                operations += 1
            for v in range(VerticalIterations):
                dot_coordinates = [((0.5+2*h)*offset, offset/2+offset+offset*2*v, offset*z/4), ((0.5+2*h)*offset, offset/2+offset*2*v, offset*z/4), ((1.5+2*h)*offset, offset/2+offset*2*v, offset*z/4), ((1.5+2*h)*offset, offset/2+offset+offset*2*v, offset*z/4)]
                plot_dots_in_box(dot_coordinates)
                operations += 1
        else:
            for v in range(VerticalIterations):
                dot_coordinates = [(2*h*offset+offset/4, offset+offset*2*v+offset/4, offset*z/4), (2*h*offset+offset/4, offset*2*v+offset/4, offset*z/4), ((1+2*h)*offset+offset/4, offset*2*v+offset/4, offset*z/4), ((1+2*h)*offset+offset/4, offset+offset*2*v+offset/4, offset*z/4)]
                plot_dots_in_box_interweaved(dot_coordinates)
                operations += 1
            for v in range(VerticalIterations):
                dot_coordinates = [((0.5+2*h)*offset+offset/4, offset/2+offset+offset*2*v+offset/4, offset*z/4), ((0.5+2*h)*offset+offset/4, offset/2+offset*2*v+offset/4, offset*z/4), ((1.5+2*h)*offset+offset/4, offset/2+offset*2*v+offset/4, offset*z/4), ((1.5+2*h)*offset+offset/4, offset/2+offset+offset*2*v+offset/4, offset*z/4)]
                plot_dots_in_box_interweaved(dot_coordinates)
                operations += 1

print("Number of Operations: " + str(operations))
print("Number of Skeins: " + str(operations*4))
#Print time of 8mm: 2:52min per Skein, 3:03min for full operation
#Print time of 10mm: 4:30min per Skein, 4:42min for full operation
print("Estimated Print Time: " + str((operations * (3*60+3))/3600) + " hours")
#Length of 10mm: 1742.2774241193479mm
#Length of 9mm: 1408.6628140280077mm
#Length of 8mm: 1110.3315252863424mm
#Length of 7mm: 847.4641796523133mm
print("Estimated Length: " + str(operations * 9 * 1110.3315252863424/1000) + " meters")
plt.show()