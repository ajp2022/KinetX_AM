import matplotlib.pyplot as plt

box_x = [0, 40, 40, 0, 0]
box_y = [0, 0, 40, 40, 0]
plt.xlim(-1, 41)
plt.ylim(-1, 41)
offset = 10.617
operations = 0

def randomcolor(i):
    if i%2==0:
        return 'bo'
    else:
        return 'ro'
    

def plot_dots_in_box(dot_coordinates):
    for x, y in dot_coordinates:
        plt.plot(x, y, 'bo', markersize = 6)
def plot_dots_in_box_interweaved(dot_coordinates):
    for x, y in dot_coordinates:
        plt.plot(x, y, 'ro', markersize = 6)

for h in range(2):
    for v in range(2):
        dot_coordinates = [(2*h*offset, offset+offset*2*v), (2*h*offset, offset*2*v), ((1+2*h)*offset, offset*2*v), ((1+2*h)*offset, offset+offset*2*v)]
        plot_dots_in_box(dot_coordinates)
        operations += 1
        
        
        x1 = 2*h*offset
        y1 = offset+offset*2*v
        X1 = f"{x1:.13f}"
        Y1 = f"{y1:.13f}"
        
        x2 = 2*h*offset
        y2 = offset*2*v
        X2 = f"{x2:.13f}"
        Y2 = f"{y2:.13f}"
        
        x3 = (1+2*h)*offset
        y3 = offset*2*v
        X3 = f"{x3:.13f}"
        Y3 = f"{y3:.13f}"
        
        x4 = (1+2*h)*offset
        y4 = offset+offset*2*v
        X4 = f"{x4:.13f}"
        Y4 = f"{y4:.13f}"
        
        print("G1  X" + str(X1) + "  Y" + str(Y1) + "  Z05.0000000000000" + "  F300.0000000000000")
        print("G1  X" + str(X1) + "  Y" + str(Y1) + "  Z00.0000000000000" + "  F120.0000000000000")
        print("G1  X" + str(X1) + "  Y" + str(Y1) + "  Z05.0000000000000" + "  F300.0000000000000")
        
        #print Skein Code Here
        
        print("G1  X" + str(X2) + "  Y" + str(Y2) + "  Z05.0000000000000" + "  F300.0000000000000")
        print("G1  X" + str(X2) + "  Y" + str(Y2) + "  Z00.0000000000000" + "  F120.0000000000000")
        print("G1  X" + str(X2) + "  Y" + str(Y2) + "  Z05.0000000000000" + "  F300.0000000000000")
        
        #print Skein Code Here
        
        print("G1  X" + str(X3) + "  Y" + str(Y3) + "  Z05.0000000000000" + "  F300.0000000000000")
        print("G1  X" + str(X3) + "  Y" + str(Y3) + "  Z00.0000000000000" + "  F120.0000000000000")
        print("G1  X" + str(X3) + "  Y" + str(Y3) + "  Z05.0000000000000" + "  F300.0000000000000")
        
        #print Skein Code Here
        
        print("G1  X" + str(X4) + "  Y" + str(Y4) + "  Z05.0000000000000" + "  F300.0000000000000")
        print("G1  X" + str(X4) + "  Y" + str(Y4) + "  Z00.0000000000000" + "  F120.0000000000000")
        print("G1  X" + str(X4) + "  Y" + str(Y4) + "  Z05.0000000000000" + "  F300.0000000000000")
        
        #print Skein Code Here
    for v in range(2):
        dot_coordinates = [((0.5+2*h)*offset, offset/2+offset+offset*2*v), ((0.5+2*h)*offset, offset/2+offset*2*v), ((1.5+2*h)*offset, offset/2+offset*2*v), ((1.5+2*h)*offset, offset/2+offset+offset*2*v)]
        plot_dots_in_box_interweaved(dot_coordinates)
        operations += 1
        
        
        x1 = (0.5+2*h)*offset
        y1 = offset/2+offset+offset*2*v
        X1 = f"{x1:.13f}"
        Y1 = f"{y1:.13f}"
        
        x2 = (0.5+2*h)*offset
        y2 = offset/2+offset*2*v
        X2 = f"{x2:.13f}"
        Y2 = f"{y2:.13f}"
        
        x3 = (1.5+2*h)*offset
        y3 = offset/2+offset*2*v
        X3 = f"{x3:.13f}"
        Y3 = f"{y3:.13f}"
        
        x4 = (1.5+2*h)*offset
        y4 = offset/2+offset+offset*2*v
        X4 = f"{x4:.13f}"
        Y4 = f"{y4:.13f}"
        
        print("G1  X" + str(X1) + "  Y" + str(Y1) + "  Z05.0000000000000" + "  F300.0000000000000")
        print("G1  X" + str(X1) + "  Y" + str(Y1) + "  Z00.0000000000000" + "  F120.0000000000000")
        print("G1  X" + str(X1) + "  Y" + str(Y1) + "  Z05.0000000000000" + "  F300.0000000000000")
        
        #print Skein Code Here
        
        print("G1  X" + str(X2) + "  Y" + str(Y2) + "  Z05.0000000000000" + "  F300.0000000000000")
        print("G1  X" + str(X2) + "  Y" + str(Y2) + "  Z00.0000000000000" + "  F120.0000000000000")
        print("G1  X" + str(X2) + "  Y" + str(Y2) + "  Z05.0000000000000" + "  F300.0000000000000")
        
        #print Skein Code Here
        
        print("G1  X" + str(X3) + "  Y" + str(Y3) + "  Z05.0000000000000" + "  F300.0000000000000")
        print("G1  X" + str(X3) + "  Y" + str(Y3) + "  Z00.0000000000000" + "  F120.0000000000000")
        print("G1  X" + str(X3) + "  Y" + str(Y3) + "  Z05.0000000000000" + "  F300.0000000000000")
        
        #print Skein Code Here
        
        print("G1  X" + str(X4) + "  Y" + str(Y4) + "  Z05.0000000000000" + "  F300.0000000000000")
        print("G1  X" + str(X4) + "  Y" + str(Y4) + "  Z00.0000000000000" + "  F120.0000000000000")
        print("G1  X" + str(X4) + "  Y" + str(Y4) + "  Z05.0000000000000" + "  F300.0000000000000")
        
        #print Skein Code Here

print("Number of Operations: " + str(operations))
print("Number of Skeins: " + str(operations*4))
print("Estimated Printing Time for a 6mm skein: " + str(operations * 3810 / 300) + " minutes")
print("Estimated Length: " + str(operations * 3.810) + " meters")
plt.show()