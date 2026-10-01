import matplotlib.pyplot as plt
import numpy as np

# grid() ▦ , ⊞ => helps to make plot easer to read by adding refrence line

x = np.array([1,2,3,4,5])
y = np.array([5,10,15,20,25])

plt.grid(axis='y' , 
         linewidth = 2,
         color = 'lightgray',
         linestyle = 'dashed')

plt.plot(x,y)
plt.show()