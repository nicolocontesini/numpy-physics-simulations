import matplotlib.pyplot as plt
import numpy as np 

t = np.linspace(0, 5, 10000)
theta = np.sin(7*t)

fig, ax = plt.subplots(figsize=(8, 5))
plt.plot(t, theta, color="#3B8040", linewidth=0.05, label='PURE SIGNAL', marker='o', markersize=1, )
ax.grid(True, linestyle='--', alpha=0.5)


#plt.text(9.75, 0.05, f"x=0", fontsize=10, color="#5407CF95", verticalalignment='center')
plt.xlabel('t')
plt.ylabel('theta')
plt.legend()
plt.yticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], ['-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5'])
plt.show()