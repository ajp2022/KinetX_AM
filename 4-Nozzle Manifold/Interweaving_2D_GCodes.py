import matplotlib.pyplot as plt

box_x = [0, 40, 40, 0, 0]
box_y = [0, 0, 40, 40, 0]
plt.xlim(-1, 51)
plt.ylim(-1, 51)
offset = 10.617
operations = 0

def randomcolor(i):
    if i%2==0:
        return 'bo'
    else:
        return 'ro'
    

def plot_dots_in_box(dot_coordinates):
    for x, y in dot_coordinates:
        plt.plot(x, y, 'bo', markersize = 10)
def plot_dots_in_box_interweaved(dot_coordinates):
    for x, y in dot_coordinates:
        plt.plot(x, y, 'ro', markersize = 10)

for h in range(2):
    for v in range(2):
        dot_coordinates = [(2*h*offset, offset+offset*2*v), (2*h*offset, offset*2*v), ((1+2*h)*offset, offset*2*v), ((1+2*h)*offset, offset+offset*2*v)]
        plot_dots_in_box(dot_coordinates)
        operations += 1
        x = ((2*h*offset)+((1+2*h)*offset))/2
        y = ((offset+offset*2*v)+(offset*2*v))/2
        X = f"{x:.13f}"
        Y = f"{y:.13f}"
        print("G1  X" + str(X) + "  Y" + str(Y) + "  Z10.0000000000000" + "  F300.0000000000000")
        print("G1  X" + str(X) + "  Y" + str(Y) + "  Z00.0000000000000" + "  F120.0000000000000")
        #print("INSERT SKEIN CODE HERE")
        print("G1  X" + str(X) + "  Y" + str(Y) + "  Z10.0000000000000" + "  F300.0000000000000")
    for v in range(2):
        dot_coordinates = [((0.5+2*h)*offset, offset/2+offset+offset*2*v), ((0.5+2*h)*offset, offset/2+offset*2*v), ((1.5+2*h)*offset, offset/2+offset*2*v), ((1.5+2*h)*offset, offset/2+offset+offset*2*v)]
        plot_dots_in_box_interweaved(dot_coordinates)
        operations += 1
        x = (((0.5+2*h)*offset)+((1.5+2*h)*offset))/2
        y = ((offset/2+offset+offset*2*v)+(offset/2+offset*2*v))/2
        X = f"{x:.13f}"
        Y = f"{y:.13f}"
        print("G1  X" + str(X) + "  Y" + str(Y) + "  Z10.0000000000000" + "  F300.0000000000000")
        print("G1  X" + str(X) + "  Y" + str(Y) + "  Z00.0000000000000" + "  F120.0000000000000")
        #print("INSERT SKEIN CODE HERE")
        print("G1  X" + str(X) + "  Y" + str(Y) + "  Z10.0000000000000" + "  F300.0000000000000")

print("Number of Operations: " + str(operations))
print("Number of Skeins: " + str(operations*4))
print("Estimated Print Time: " + str(operations * 3810 / 300) + " minutes")
print("Estimated Length: " + str(operations * 3.810) + " meters")
plt.show()