import matplotlib.pyplot as plt
import numpy as np

# pie chart 🍕 => circular chart divided into slices to show percentage of the total.
# good for visualizing distribution amoung categories
 
 
categories = np.array(['freshmen' , 'sophomores' , 'juniors' , 'seniors'])
values = np.array([300 , 250, 275,225])
colors = ['red' , 'yellow','blue','green']

plt.pie(values , 
        labels=categories,
        autopct='%1.1f%%' , 
        colors=colors,
        explode=[0,0,0,0.1],
        shadow=True,
        startangle=90)

plt.title('my collage')
plt.show()