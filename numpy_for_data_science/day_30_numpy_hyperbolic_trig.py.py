#trigonometric function- numpy provides the ufuncs line sine, cos, and tan

#that take value in radian and produce the corresponding sin(), cos(), and tan() value.

#Here now we will find the sine value of pi/2

import numpy as np
sharad = np.sin(np.pi/2)
Print(sharad)

#We will now find the sine value of an array

import numpy as np
sharad = np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
sharadnew = np.sin(sharad)
Print(sharadnew)

#convert degree - into radian by default all of the trigonometric function takes radians as parameter.

#Note- radians value are  pi/180 degree values.

#Here we will convert all the error value to radians.

import numpy as np
sharad = np.array([90,180,270,360])
sharadnew = np.deg2rad(sharad)
Print(sharadnew)

#Here we will convert radians into degree.

import numpy as np
sharad = np.array([np.pi/2,np.pi,1.5*np.pi,2*np.pi])
sharadnew = np.deg2rad(sharad)
Print(sharadnew)

#Here we will also find angles - arcsin(), arccos(), and arctan()

#that take value in radians and produce the corresponding sin, cos, and tan values.

#We will now find the angle of 1.0

import numpy as np
sharad = np.arcsin(1.0)
Print(sharad)

#angles of each  values in an array.

import numpy as np
sharad = np.array([1, -1, 0.1])
sharadnew = np.arcsin(sharad)
Print(sharadnew)

#Here we will also find the hypotenuse using the Pythagoras theorem in numpy,

#hypot() function that take value in radians and produce the corresponding sin, cos, and tan values.

#Here we will find the hypot for 3 base and 4 perpendicular.

import numpy as np
base = 3
perpendicular = 4
sharad = np.hypot(base,prep)
Print(sharad)








