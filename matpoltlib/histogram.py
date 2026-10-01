import matplotlib.pyplot as plt
import numpy as np

# histogram 📶 => A visual represntation of the distribution of qunatitaive data .
# they group values into bins(intervals)
# and count how many falls in each range 

scores = np.random.normal(loc = 80 , scale=10 , size=100)
scores = np.clip(scores , 0,100)

plt.hist(scores , bins=10,
         color="lightgray",
         edgecolor = 'black')

plt.title('Exam marks')
plt.xlabel('scores')
plt.ylabel('no of students')

plt.show() 