import matplotlib.pyplot as plt
import numpy as np

# bar chart 📊 => compare categories of data by represnting each catagory

catagories = np.array(['grains' , 'vegitable' , 'protein' , 'dairy' ,'sweet'])
values = np.array([3,2,1,2,5])

plt.bar(catagories,values , color='skyblue')
# plt.barh(catagories,values , color='skyblue')   horizonatl chart

plt.title('Daily consumpation')
plt.xlabel('catagory')
plt.ylabel('values')
plt.show()


