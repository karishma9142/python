import numpy as np

# aggregate function. => summerzie data and typicallt return a single value

array = np.array([[1,2,3,4],
                  [5,6,7,8]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array))  # standard devation
print(np.var(array)) # ariance = square of standard devation
print(np.min(array))
print(np.max(array))
print(np.argmin(array)) # position of minimum argumnet value
print(np.argmax(array)) # position of maximum argumnet value

print(np.sum(array , axis=0)) #rows sum
print(np.sum(array , axis=1)) #cols sum