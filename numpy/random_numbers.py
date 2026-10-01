import numpy as np

rng = np.random.default_rng(seed=1) # repuduce same number

print(rng.integers(low=1,high=101,size=(3,2)))

# floating number

print(np.random.uniform(low=1,high=100,size=(3)))


# shuffke array

array = np.array([1,2,3,4,5])

rng2 = np.random.default_rng()
rng2.shuffle(array)
print(array)


# choise

frutes = np.array(['apple' , 'banana','coconut','orange','pinapple'])
frute = rng2.choice(frutes , size=(3,2))
print(frute)