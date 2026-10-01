import numpy as np

''''
broadcastion allows python to perfrom operation on array
with deffernet shapes by vertually expanding dainmensions
so they larger array shape

the daimension have the same size
or
one of the daimension have the size of 1
'''

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3],[4]])

print(array1.shape)
print(array2.shape)

array3 = array1*array2
print(array3.shape)
print(array3)