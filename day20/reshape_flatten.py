import numpy as np
a=np.array([1,2,3,4,5,6])


b=a.reshape(2,-1)
print(a)
print(b)


c=a.reshape(3,-1)
print(c)

print(b.flatten())
print(c.flatten())

print(b.ravel())