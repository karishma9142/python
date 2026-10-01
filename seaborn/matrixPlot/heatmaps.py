import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

cs_df = pd.read_csv('../computerSale.csv')

# plt.figure(figsize=(8,6))
# sns.set_context('paper' , font_scale=1.4)
# cs_max = cs_df.select_dtypes(include=np.number).corr()

# sns.heatmap(cs_max , annot=True , cmap='Blues')

cs = cs_df
cs = cs.pivot_table(index='Sale Price' , columns='Age' , values='Profit')
sns.heatmap(cs , cmap='Blues' , linecolor='white' , linewidths=1)
plt.show()