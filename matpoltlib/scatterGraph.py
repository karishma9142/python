import matplotlib.pyplot as plt
import numpy as np

# scatter graph 🔵 => shows the relationship between two variables , helps in identify a corelation (+ ,- ,none)
# ex -> study hours Vs test scores

x = np.array([0,1,1,2,5,6,8,8])
y = np.array([55,60,65,62,68,70,75,78])

x2 = np.array([0,1,1,2,5,6,8,8])
y2 = np.array([55,66,66,72,68,75,79,88])

plt.scatter(x,y , color='skyblue' , alpha=0.5 , s=100)
plt.scatter(x2,y2,color='red' , alpha=0.5,s=100)

plt.title('test scores')
plt.xlabel('study hours')
plt.ylabel('scores')
plt.show()

