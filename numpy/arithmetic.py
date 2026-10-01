import numpy as np

array = np.array([1,2,3])

# print(array+2)
# print(array-2)
# print(array*2)
# print(array/2)
# print(array%2)
# print(array**2)

# vectorized maath function

array2 = np.array([1.1,2.9,3.3])

# print(np.sqrt(array2))
# print(np.round(array2))
# print(np.floor(array2))
# print(np.ceil(array2))

# print(np.pi)



# element vise arithmetic

array3 = np.array([1,2,3])
array4 = np.array([4,5,6])

# print(array3 + array4)
# print(array3 - array4)
# print(array3 * array4)
# print(array3 / array4)
# print(array3 ** array4)



# comparison operator

scores = np.array([55,60,100,90,80])

print(scores == 100)
print(scores >= 60)
scores[scores<60] = -1
print(scores)