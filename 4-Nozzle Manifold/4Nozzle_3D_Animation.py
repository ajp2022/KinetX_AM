import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1, 51)
ax.set_ylim(-1, 51)
ax.set_zlim(-1, 51)

offset = 10.617
operations = 0
dot_operations = []

for z in range(4):
    for h in range(2):
        for v in range(2):
            dot_coordinates = [(2 * h * offset, offset + offset * 2 * v, z*offset), (2 * h * offset, offset * 2 * v, z*offset), ((1 + 2 * h) * offset, offset * 2 * v, z*offset), ((1 + 2 * h) * offset, offset + offset * 2 * v, z*offset)]
            dot_operations.append((dot_coordinates, 'bo'))
            operations += 1
        for v in range(2):
            dot_coordinates = [((0.5 + 2 * h) * offset, offset / 2 + offset + offset * 2 * v, z*offset), ((0.5 + 2 * h) * offset, offset / 2 + offset * 2 * v, z*offset), ((1.5 + 2 * h) * offset, offset / 2 + offset * 2 * v, z*offset), ((1.5 + 2 * h) * offset, offset / 2 + offset + offset * 2 * v, z*offset)]
            dot_operations.append((dot_coordinates, 'ro'))
            operations += 1

def update(frame):
    dot_coordinates, color = dot_operations[frame]
    xs, ys, zs = zip(*dot_coordinates)
    ax.scatter(xs, ys, zs, c=color[0])

ani = FuncAnimation(fig, update, frames=len(dot_operations), interval=250, repeat=False)

print("Number of Operations: " + str(operations))
print("Number of Skeins: " + str(operations*4))
print("Estimated Printing Time for a 6mm skein: " + str(operations * 3810 / 300) + " minutes")
print("Estimated Length: " + str(operations * 3.810) + " meters")

plt.show()