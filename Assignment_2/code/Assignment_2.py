
import matplotlib.pyplot as plt
import numpy as np
import math as m
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(211, projection='3d')# subplot for Plane
normal=np.array([3,5,-6])
d=7/m.sqrt(70)
xx,yy=np.meshgrid(range(50),range(50))
z = (-normal[0]*xx -normal[1]*yy -d)*1./normal[2]
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx,yy,z, color='blue')
ax = fig.add_subplot(212, projection='3d')#subplot for normal vector

x_pos = 0
y_pos = 0
x_direct = 3
y_direct = 5
z_pos=0
z1_direct=-6

ax.quiver(x_pos,y_pos,x_direct,y_direct,z_pos,z1_direct)


plt.show()
Axes3D.plot()