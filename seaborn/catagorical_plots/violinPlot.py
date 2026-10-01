import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

cs_df = pd.read_csv('../computerSale.csv')

sns.violinplot(x='Age' , y='Year' , data = cs_df, hue='Sex', split=True)
plt.legend(loc=0)
plt.show()