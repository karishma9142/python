import numpy as np

# filtering => refresh to the process of selecting elements from ans aaray that matches a given condition

ages = np.array([[13,65,45,98,35,65,90,56],
                 [23,15,76,20,17,43,67,45]])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages<65)] 
evens = ages[ages%2 == 0]
odds = ages[ages%2 != 0]

seniors = np.where(ages>=65 , ages , -1)

print(teenagers)
print(adults)
print(evens)
print(odds)
print(seniors)