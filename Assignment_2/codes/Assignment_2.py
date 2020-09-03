"""Find the equation of a plane which is at 7 units distance from
origin and normal to the vector a"""
import numpy as np
a=np.array([3,5,-6])
b=7
c=np.linalg.norm(a)
d=b*c
print("The equation of plane is {0}.f = {1} & f is the position vector".format(a,d))
#


