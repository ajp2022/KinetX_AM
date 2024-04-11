import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

output_file_path = "3D_4Nozzle_Test1.gcode"
output_file = open(output_file_path, "w")

def generated_beginning_gcode():
    gcode = """
;Generated by Cura LulzBot Edition GCodeWriter Version: 3.6.37
;FLAVOR:Marlin
;TIME:1731
;Filament used: 0.807459m
;Layer height: 0.38
;Generated with Cura_SteamEngine 3.6.37-win10
M82 ;absolute extrusion mode
;This G-Code has been generated specifically for the LulzBot TAZ 5 with standard extruder
M75			 ; start GLCD timer
G90                      ; absolute positioning
M107                     ; disable fans
M117 Heating...                     ; progress indicator message on LCD
G1 F175       ; set travel speed
M203 X192 Y208 Z3        ; set limits on travel speed
M117 40 min double helix ; progress indicator message on LCD
"""
    return gcode
def generated_end_gcode():
    gcode = """
M140 S0
M107
M400                         ; wait for moves to finish
M107                         ; disable fans
G91                          ; relative positioning
M77			     ; stop GLCD timer
G90                          ; absolute positioning
M84                          ; disable steppers
G90                          ; absolute positioning
M117 Print Complete.                      ; print complete message
M82 ;absolute extrusion mode
M104 S0
;End of Gcod
    """
    return gcode

box_x = [0, 50, 50, 0, 0]
box_y = [0, 0, 60, 60, 0]
plt.xlim(0, 50)
plt.ylim(0, 50)
offset = 10.617
operations = 0

def plot_dots_in_box(dot_coordinates):
    for x, y in dot_coordinates:
        plt.plot(x, y, 'bo', markersize = 10)
def plot_dots_in_box_interweaved(dot_coordinates):
    for x, y in dot_coordinates:
        plt.plot(x, y, 'ro', markersize = 10)

def skein(x_coord, y_coord, z_coord):
    # Parameters for the path calculation
    step = 0.1  # resolution, time step period for each xyz calculation
    k = 4
    dp = 0.08  # change to modify ER, minimum distance between fibers, center to center
    h = 0.3  # height of each layer
    c1 = 2  # standard deviation coefficient
    H = 8  # total height of the skin


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
    output_file.write(skeingcode)

HeightLayers = 4 #True layer height is HeightLayers-1
HorizontalIterations = 4
VerticalIterations = 4

output_file.write(generated_beginning_gcode())

#Skein Code
for z in range(1,HeightLayers):
    for h in range(HorizontalIterations):
        if z % 2 != 0:
            for v in range(VerticalIterations):
                operations += 1
                x = (0.5+2*h)*offset
                y = (0.5+2*v)*offset
                z_new = (offset*z/3)
                zexit = (offset*z/3) + 8 + 3
                X = f"{x:.13f}"
                Y = f"{y:.13f}"
                Z = f"{z_new: .13f}"
                Zexit = f"{zexit: .13f}"
                output_file.write("G1  X" + str(X) + "  Y" + str(Y) + "  Z" + str(Z) + "  F120.0000000000000\n")
                output_file.write("M106S255\n")
                skein(x, y, z_new)
                output_file.write("M107\n")
                output_file.write("G1  X" + str(X) + "  Y" + str(Y) + "  Z" + str(Zexit) + "  F300.0000000000000\n") # remember to put height in there, Adam parametrize this
            for v in range(VerticalIterations):
                operations += 1
                x = (1+2*h)*offset
                y = (1+2*v)*offset
                z_new = (offset*z/3)
                zexit = (offset*z/3) + 8 + 3
                X = f"{x:.13f}"
                Y = f"{y:.13f}"
                Z = f"{z_new: .13f}"
                Zexit = f"{zexit: .13f}"
                output_file.write("G1  X" + str(X) + "  Y" + str(Y) + "  Z" + str(Z) + "  F120.0000000000000\n")
                output_file.write("M106S255\n")
                skein(x, y, z_new)
                output_file.write("M107\n")
                output_file.write("G1  X" + str(X) + "  Y" + str(Y) + "  Z" + str(Zexit) + "  F300.0000000000000\n")
        else:
            for v in range(VerticalIterations):
                operations += 1
                x = (0.5+2*h)*offset+offset/4
                y = (0.5+2*v)*offset+offset/4
                z_new = (offset*z/3)
                zexit = (offset*z/3) + 8 + 3
                X = f"{x:.13f}"
                Y = f"{y:.13f}"
                Z = f"{z_new: .13f}"
                Zexit = f"{zexit: .13f}"
                output_file.write("G1  X" + str(X) + "  Y" + str(Y) + "  Z" + str(Z) + "  F120.0000000000000\n")
                output_file.write("M106S255\n")
                skein(x, y, z_new)
                output_file.write("M107\n")
                output_file.write("G1  X" + str(X) + "  Y" + str(Y) + "  Z" + str(Zexit) + "  F300.0000000000000\n")
            for v in range(VerticalIterations):
                operations += 1
                x = (1+2*h)*offset+offset/4
                y = (1+2*v)*offset+offset/4
                z_new = (offset*z/3)
                zexit = (offset*z/3) + 8 + 3
                X = f"{x:.13f}"
                Y = f"{y:.13f}"
                Z = f"{z_new: .13f}"
                Zexit = f"{zexit: .13f}"
                output_file.write("G1  X" + str(X) + "  Y" + str(Y) + "  Z" + str(Z) + "  F120.0000000000000\n")
                output_file.write("M106S255\n")
                skein(x, y, z_new)
                output_file.write("M107\n")
                output_file.write("G1  X" + str(X) + "  Y" + str(Y) + "  Z" + str(Zexit) + "  F300.0000000000000\n")

    
    output_file.write(generated_end_gcode())

#2D Simulation Code
for h in range(HorizontalIterations):
    for v in range(VerticalIterations):
        dot_coordinates = [(2*h*offset, offset+offset*2*v), (2*h*offset, offset*2*v), ((1+2*h)*offset, offset*2*v), ((1+2*h)*offset, offset+offset*2*v)]
        plot_dots_in_box(dot_coordinates)
    for v in range(VerticalIterations):
        dot_coordinates = [((0.5+2*h)*offset, offset/2+offset+offset*2*v), ((0.5+2*h)*offset, offset/2+offset*2*v), ((1.5+2*h)*offset, offset/2+offset*2*v), ((1.5+2*h)*offset, offset/2+offset+offset*2*v)]
        plot_dots_in_box_interweaved(dot_coordinates)

#print("Number of Operations: " + str(operations))
#print("Number of Skeins: " + str(operations*4))
#print("Estimated Print Time: " + str(operations * 3810 / 300) + " minutes")
#print("Estimated Length: " + str(operations * 3.810) + " meters")
#plt.show()

output_file.close()