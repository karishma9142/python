import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

# slicing. => 
# array[start : end : step]
# array[rows => start : end : step , cols=>start : end : step]

# for rows slicing

# print(array)
# print(array[1:3])
# print(array[0:3:2])
# print(array[::2])
# print(array[::-1]) reversed 

# for coloum slicing

# print(array[:,1])
# print(array[:,-1])
# print(array[:,1:3])
# print(array[:,::2])
# print(array[:,::-2])
print(array[0:2,0:2])


