import numpy as np
import matplotlib.pyplot as plt

print("0 <= theta < 90 and v0 >= 0 and y0 >= 0")
while True:
    try:
        Dtheta = float(input("theta (deg) = ")) 
        theta = np.radians(Dtheta) #only as input (user friendly :) )
        if 0 <= theta < 90:
            break
        else:
             raise NameError
    except ValueError, NameError:
        pass

while True:
    try:
        v0 = float(input("v0 (m/s) = "))
        if 0 <= v0:
            break
        else:
             raise NameError
    except ValueError, NameError:
        pass

while True:
    try:
        y0 = float(input("y0 (m) = "))
        if y0 >= 0:
            break
        else:
            raise NameError
    except ValueError, NameError:
        pass
    
theta = np.radians(Dtheta) #only as input (user friendly :) )
v0_x = v0 * np.cos(theta)
v0_y = v0 * np.sin(theta)
g = 9.81


#graph
R_flat = (2 * v0**2 * np.cos(theta) * np.sin(theta)) / g   #range for same level --  -- 
R_ground = (v0_y + np.sqrt(v0_y**2 + 2*g*y0))*(v0_x / g)   #range to the x-axis |__

x = np.arange(0, R_ground, 0.001)
y = y0 + x * np.tan(theta) - (1/2) * g * (x / (v0 * np.cos(theta)))**2

fig, ax = plt.subplots(figsize=(8, 5))
# Traccia la linea sul piano cartesiano
ax.plot(x, y, color="#3B8040", linewidth=1, marker='o', markersize=3)
ax.grid(True, linestyle='--', alpha=0.5)
plt.xlabel('distance')
plt.ylabel('height')





#useful :)
A_x = (v0**2 * np.cos(theta) * np.sin(theta)) / g
A_y = y0 + A_x * np.tan(theta) - (1/2) * g * (A_x / (v0 * np.cos(theta)))**2

plt.text(A_x + 0.2, A_y + 0.2, f'Apex', fontsize=10, verticalalignment='center')



plt.plot(A_x, A_y, 'ro')
ax.plot(x, y, color="#3B8040", linewidth=2, marker='o', markersize=3)
R_points_x = np.array([0, R_ground])
R_y = np.array([0, 0])

plt.plot(R_points_x, R_y, color="#5407CF95", linewidth=1, linestyle = 'dashed')
plt.text(A_x, 0.5, f'RANGE', fontsize=10, color="#5407CF95", verticalalignment='center')


plt.show()


