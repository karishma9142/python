import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

cs_df = pd.read_csv('../computerSale.csv')

plt.figure(figsize=(8,5))
sns.set_style('dark')
sns.set_context('talk')

sns.stripplot(x='Age' , y='Profit' , data=cs_df , hue='Sex' , palette='magma')
plt.show()