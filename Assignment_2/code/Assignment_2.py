
import matplotlib.pyplot as plt
import numpy as np
import math as m
from mpl_toolkits.mplot3d import Axes3D
fig
ax = fig.add_subplot(311, projection='3d')# subplot for Plane
normal=np.array([3,5,-6])
d=7*m.sqrt(70)
# a plane is a*x+b*y+c*z+d=0
# [a,b,c] is the normal. Thus, we have to calculate
# d and we're set
d = -7*m.sqrt(70)

# create x,y
xx, yy = np.meshgrid(range(30), range(30))

# calculate corresponding z
z = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2]

# plot the surface
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx, yy, z)
ax = fig.add_subplot(312, projection='3d')# subplot for Plane
normal=np.array([3,5,-6])
# a plane is a*x+b*y+c*z+d=0
# [a,b,c] is the normal. Thus, we have to calculate
# d and we're set
d = 7*m.sqrt(70)

# create x,y
xx, yy = np.meshgrid(range(30), range(30))

# calculate corresponding z
z = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2]

# plot the surface
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx, yy, z)

fig=plt.figure()

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
