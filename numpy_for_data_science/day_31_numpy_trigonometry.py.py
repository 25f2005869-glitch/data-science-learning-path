#hyperbolic function- numpy provides the ufuncs line sine, cos, and tan

#that take value in radian and produce the corresponding sin(), cos(), and tan() value.

#Here now we will find the sinh value of pi/2

import numpy as np
sharad = np.sinh(np.pi/2)
Print(sharad)

#We will now find the cosh value of an array

import numpy as np
sharad = np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
sharadnew = np.cosh(sharad)
Print(sharadnew)

#finding angles:

#Here we will also find angles - arcsinh(), arccosh(), and arctanh()

#that take value in radians and produce the corresponding sinh, cosh, and tanh values.

#We will now find the angle of 1.0

import numpy as np
sharad = np.arcsinh(1.0)
Print(sharad)

#angles of each  values in an array.

import numpy as np
sharad = np.array([ 0.1, 0.2, 0.5])
sharadnew = np.arcsinh(sharad)
Print(sharadnew)



















