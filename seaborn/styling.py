import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

cs_df = pd.read_csv('computerSale.csv')

sns.set_style('darkgrid')
plt.figure(figsize=(4,4))
sns.jointplot(x='Sale Price' , y='Profit' , data=cs_df , kind='reg')
sns.set_context('paper' , font_scale=1.5)
plt.show()